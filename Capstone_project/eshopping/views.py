from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Item, Category, ProductImage, User, ShoppingCart, PlacedOrder, OrderStatus
import json
from .util import no_item_per_page, check_exist_shopping_cart

    
# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "eshopping/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "eshopping/login.html")
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "eshopping/register.html", {
                "message": "Passwords must match."
            })
        if password =='':
            return render(request, "eshopping/register.html", {
                "message": "Passwords must not be empty."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "eshopping/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "eshopping/register.html")

def index(request):
    # Get all category
    categories = Category.objects.all()

    # Get all item
    items = Item.objects.all()
    p = Paginator(items,no_item_per_page)

    return render(request, "eshopping/index.html",{
        "category": categories,
        "total_page_no": p.num_pages,
        "box_no": no_item_per_page,
        "no_box_range": range(no_item_per_page)
    })


def page_content(request, page_no, category_id):
    # print(page_no)
    # print(category_id)
    if category_id == 0:
        items = Item.objects.all()
    else:
        selected_category = Category.objects.get(pk=category_id)
        items = Item.objects.filter(category=selected_category)
    p = Paginator(items, no_item_per_page)
    page_obj = p.get_page(page_no)
    json_data = serializers.serialize("json", page_obj)
    return JsonResponse(json_data, safe=False)


def total_page_no_filter(request, category_id):
    # print(category_id)
    if category_id == 0 :
        items = Item.objects.all()
    else:
        selected_category = Category.objects.get(pk=category_id)
        items = Item.objects.filter(category=selected_category)
    p = Paginator(items, no_item_per_page)
    total_no = p.num_pages
    return JsonResponse(total_no, safe=False)


def item_search(request):
    search_text = str(request.GET['search_text'])
    items = Item.objects.filter(name__icontains=search_text)
    #print(items)
    if not items:
        #print("nothing")
        match = False
        total_page_no = 0
    else:
        match = True
        p = Paginator(items, no_item_per_page)
        total_page_no = p.num_pages
    return render(request, "eshopping/search_result.html",{
        "match": match,
        "box_no": no_item_per_page,
        "no_box_range": range(no_item_per_page),
        "total_page_no": total_page_no,
        "search_text": search_text
    })


def item_detail(request, id):
    if request.method == "GET":
        # Get item detail
        # print(id)
        item = Item.objects.get(pk=id)
        small_images = ProductImage.objects.filter(product=item)
        #print(small_images)
        return render(request, "eshopping/details.html",{
            "item": item,
            "small_images": small_images
        })
    

def search_page_content(request, page_no, search_text):
    items = Item.objects.filter(name__icontains=search_text)
    p = Paginator(items, no_item_per_page)
    page_obj = p.get_page(page_no)
    json_data = serializers.serialize("json", page_obj)
    return JsonResponse(json_data, safe=False)


@csrf_exempt
@login_required(login_url='login')
def add_shopping_cart(request, item_id):
    if request.method == "POST":
        data = json.loads(request.body)
        quantity = data.get("quantity", "")
        if int(quantity) <= 0 :
            return JsonResponse({"error": "Quantity should be greater than 0."}, status=400)
        item = Item.objects.get(pk=item_id)
        user = User.objects.get(pk=request.user.id)
        if not check_exist_shopping_cart(user, item):
            cart = ShoppingCart(
                buyer = user,
                wished_item = item,
                quantity = quantity
            )
            cart.save()
        else:
            cart = ShoppingCart.objects.get(buyer=user, wished_item=item)
            cart.quantity = int(cart.quantity) + int(quantity)
            cart.save()

        return JsonResponse({"message": "Item is added to shopping cart successfully."}, status=201)
    else:
        return JsonResponse({"error": "POST request required."}, status=400)
    
@login_required(login_url='login')
def view_shopping_cart(request):
    user = User(id=request.user.id)
    cart = ShoppingCart.objects.filter(buyer=user)
    if not cart:
        no_type_item = 0
    else:
        no_type_item = cart.count()
        
    return render(request, "eshopping/shopping_cart.html", {
        "carts": cart
    })


@csrf_exempt
def edit_shopping_cart_item_no(request, item_id):
    if request.method == "GET":
        user = User.objects.get(pk=request.user.id)
        item = Item.objects.get(pk=item_id)
        cart = ShoppingCart.objects.get(buyer=user, wished_item=item)
        quantity = str(cart.quantity)
        #print(quantity)
        return JsonResponse(quantity, safe=False)
    if request.method == "POST":
        data = json.loads(request.body)
        quantity = data.get("quantity", "")
        item = Item.objects.get(pk=item_id)
        user = User.objects.get(pk=request.user.id)
        cart = ShoppingCart.objects.get(buyer=user, wished_item=item)
        if int(quantity) == 0 :
            cart.delete()
            return JsonResponse({"message": "Item is removed from shopping cart successfully."}, status=201)
        else:
            cart.quantity = int(quantity)
            cart.save()
            return JsonResponse({"message": "Item is added to shopping cart successfully."}, status=201)
        
@login_required(login_url='login')
def placing_order(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        carts = ShoppingCart.objects.filter(buyer=user)

        # Place order to model
        for cart in carts:
            status =  OrderStatus.objects.get(pk=3)
            order = PlacedOrder()
            order.buyer = user
            order.product = cart.wished_item
            if cart.wished_item.updated_price:
                order.product_price = cart.wished_item.updated_price
            else:
                order.product_price = cart.wished_item.price
            order.quantity = cart.quantity
            order.status = status
            order.save()

        # remove item from shopping cart
        for cart in carts:
            cart.delete()
        return HttpResponseRedirect(reverse("index"))
    
@login_required(login_url='login')
def user_profile(request):
    user = User.objects.get(pk=request.user.id)
    order = PlacedOrder.objects.filter(buyer=user)
    return render(request, "eshopping/profile.html", {
                "current_user": user,
                "orders": order
            })


@csrf_exempt
def stock_check(request, item_id):
    if request.method == "GET":
        item = Item.objects.get(pk=item_id)
        return JsonResponse(item.stock, safe=False)
    if request.method == "POST":
        data = json.loads(request.body)
        stock = data.get("stock", "")
        item = Item.objects.get(pk=item_id)
        item.stock = stock
        item.save()
        return JsonResponse({"message": "Stock is updated successfully."}, status=201)

@staff_member_required(login_url='protected_view')
def staff_view(request):
    return render(request, "eshopping/staff_view.html")


def protected_view(request):
    return render(request, "eshopping/protected_view.html")

@staff_member_required(login_url='protected_view')
def order_manage(request):
    status_id = int(request.GET['status_id'])
    # print(status_id)
    if status_id == 0 :
        orders = PlacedOrder.objects.all().order_by('-time')
        load_option = 0
    else:
        order_status = OrderStatus.objects.get(pk=status_id)
        orders = PlacedOrder.objects.filter(status=order_status).order_by('-time')
        load_option = 1
    
    status = OrderStatus.objects.all()

    return render(request,  "eshopping/order_manage.html", {
        "orders": orders,
        "order_status": status,
        "load_option": load_option
    })


@csrf_exempt
def order_detail(request, order_id):
    if request.method == "GET":
        order = PlacedOrder.objects.filter(pk=order_id)
        print(order)
        json_data = serializers.serialize("json", order)
        return JsonResponse(json_data, safe=False)
    if request.method == "POST":
        order = PlacedOrder.objects.get(pk=order_id)
        data = json.loads(request.body)
        price = data.get("price", "") 
        quantity = data.get("quantity", "") 
        status = data.get("status", "")
        if int(quantity) > 0:
            order.product_price = price
            order.quantity = quantity
            order_status = OrderStatus.objects.get(pk=status)
            order.status = order_status
            order.save()
            return JsonResponse({"message": "Order is updated successfully."}, status=201)
        else:
            order.delete()
            return JsonResponse({"message": "Order is deleted successfully."}, status=201)
    

@staff_member_required(login_url='protected_view')
def customer_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    order = PlacedOrder.objects.filter(buyer=user)
    return render(request, "eshopping/profile.html", {
                "current_user": user,
                "orders": order
            })


@staff_member_required(login_url='protected_view')
def stock_manage(request):
    items = Item.objects.all()
    outstanding_list=[]
    for item in items:
        orders = PlacedOrder.objects.filter(product=item, status=2)|PlacedOrder.objects.filter(product=item, status=3)
        no_outstanding = 0
        for order in orders:
            no_outstanding = no_outstanding + order.quantity
        #print(no_outstanding)
        outstanding_list.append(dict(item_id = item.id, quantity = no_outstanding))
    return render(request, "eshopping/stock_manage.html", {
        "items": items,
        "outstanding_list":outstanding_list
    })