from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User, Post, Follow
from .util import check_followed


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['writer','content']


def index(request):
    return HttpResponseRedirect(reverse("all_post"))


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required(login_url='login')
def new_post(request):
    if request.method == "POST":
        if request.user.id != int(request.POST["writer"]):
            return render(request, "network/error.html",{
                    'message': "Error"
                })
        form = PostForm(request.POST)
        if form.is_valid():
            #print('pass')
            form.save()
        else:
            print(form.errors)
            return render(request, "network/error.html",{
                    'message': "Error"
                })
        return HttpResponseRedirect(reverse("index"))
    

def all_post(request):
    post = Post.objects.all().order_by('-time')
    p = Paginator(post,10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, "network/index.html",{
        "post_list": page_obj
    })


def profile(request, user_id):
    # get user post list
    user = User.objects.get(id = user_id)
    no_being_follow = Follow.objects.filter(be_followed = user_id).count()
    no_to_follow = Follow.objects.filter(to_follow = user_id).count()
    # check request user = profile user
    if request.user.id:
        if request.user.id == user_id:
            same = True
        else:
            same = False
    else:
        same = True

    # check if request user has followed the profile user
    has_followed = check_followed (request.user.id, user_id)

    list = user.post.all().order_by('-time')
    p = Paginator(list,10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    return render(request, "network/profile.html",{
        "user_id": user.id,
        "username": user.username,
        "user_post": page_obj,
        "same_user": same,
        "being_follow": no_being_follow,
        "to_follow": no_to_follow,
        "has_followed": has_followed
    })


@login_required(login_url='login')
def follow(request, user_id):
    follow = Follow()
    follow.to_follow = User.objects.get(id=request.user.id)
    follow.be_followed = User.objects.get(id=user_id)
    follow.save()
    return redirect(profile, user_id=user_id)


@login_required(login_url='login')
def unfollow(request, user_id):
    follow = Follow.objects.get(to_follow=request.user.id, be_followed=user_id).delete()
    return redirect(profile, user_id=user_id)


@login_required(login_url='login')
def following(request):
    # get who user is followed by the request user
    followed_user = Follow.objects.filter(to_follow=request.user.id)
    #print(followed)
    followed_post = Post.objects.none()
    for user in followed_user:
        post_list = Post.objects.filter(writer=user.be_followed)
        followed_post = followed_post|post_list
    followed_post=followed_post.order_by('-time')
    p = Paginator(followed_post,10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, "network/following.html",{
        "user_post": page_obj
    })

@csrf_exempt
@login_required
def edit(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    
    if request.method == "GET":
        return JsonResponse(post.serialize())
    
    if request.method == "POST":
        data = json.loads(request.body)
        # content cannot be empty
        if data.get("content") == [""]:
            return JsonResponse({"error": "Content cannot be empty."}, status=400)
        
        # check request user is the post writer or not
        if data.get("writer") != request.user.id:
            return JsonResponse({"error": "Request user is not the post owner."}, status=400)
          
        # update Post value
        post = Post.objects.get(pk=id)
        post.content = data.get("content")
        post.save()

        return JsonResponse({"message": "Post edited successfully."}, status=201)
    
@csrf_exempt
@login_required
def like_post(request, id):
    if request.method == "POST":
        data = json.loads(request.body)

        # Update post like no
        post = Post.objects.get(pk=id)
        post.like_no = data.get("like_no")

        # Update the request user has liked the post
        post.liked_user.add(User.objects.get(pk=request.user.id))
        post.save()
        return JsonResponse({"message": "Post edited successfully."}, status=201)


@csrf_exempt
@login_required
def unlike_post(request, id):
    if request.method == "POST":
        data = json.loads(request.body)

        # Update post like no
        post = Post.objects.get(pk=id)
        post.like_no = data.get("like_no")

        # Update the request user has unliked the post
        post.liked_user.remove(User.objects.get(pk=request.user.id))
        post.save()
        return JsonResponse({"message": "Post edited successfully."}, status=201)