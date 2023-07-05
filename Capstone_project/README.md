# Eshopping

## Background
It is a web application which created by Django framework. This web application is called "Eshopping". It is online shopping application. Shop owner can put the product information into the web application. Customer can view what products are available. Customer can place order to buy the product. Owner and then can contact the customer for further action (payment method, delivery method) 

## Distinctiveness and Complexity
This project "Eshopping" seems to be appeared to be the project2 "Commerce". While extra functions and user-friendness feautures has been added to this project. Below session will explain what functions and features has been implemented in this project and how this project is different from projec2 "Commerce".

### Extra functions - User side
* shopping cart: Users can add products to the shopping cart first before they really place the order. User can also edit the shopping cart (change the quantity or remove items). When user has confirmed what items and the quantity, they can press the "place order" button to place the order. The shop owner will know the order has been placed and further action will be made by the owner.

* order history: Users can view their order history. They can view what orders they has been placed. They can also know the order status, i.e. their order is delivered, delivery is on-going, waiting payment, etc. 

### Extra functions - Shop owner side
Although shop owner can use Django bulit-in admin site to manage the eshopping site, some functions has been added to the project so that it makes some daily managment activities more user friendly.

* Order management: Owner can manage the orders placed by customers. Owner can view the details of the orders. Owner can also edit the order details(e.g. change quantity from customer's request). Owner can also update the order status(e.g. if customer has paid and the product has been shipped out, then owner can update the status to "delivery is on-going").

* Stock management: Owner can manage product stock. Owner can view the current stock of all their product. Owner can also know what quantity of each product is needed from outstanding orders. Owner can also update the stock.

### User-friendness feautures
* page navigation: In the main(index) page, user can view what products are available on site. The page shows 9 products at once. If no. of products is larger than 9, the rest of them will be shown in other pages. User can view them by using the page navigation. The page-navigation is using javascript and API to update the page content. The page does not reload entirety. 

* product search: User can search the product by inputing the keyword in search box.

## Project structure
Below is a list of files which I have created

### Folder "capstone/eshopping/static/eshopping/"

#### detail_image_display.js :

It is a javascript file which contains the functions for displaying and swapping the images of product in the detail.html.

```
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', event => {
        const element = event.target;
        if (element.className === "small_image"){
            ...
        }
    });
});
```
When the user clicks a image inside the ```small_image``` div of detail.html, the code will swap the clicked image with the image in ```large_image``` div.  

```
function ImagePositionSwap(BeSwapId, ToSwapId") {
    ...
}
```
The function takes ```BeSwapId``` and ```ToSwapId``` as arguments. The arguments are the id of the images of "being swapped" and "to swap".

#### item_box_content.js :

It is a javascript file which contains the functions for displaying the product information in the grid box inside the index page and search result page. 

```
function item_box_content(box_name, item) {
    ...
}
```
The function takes ```box_name``` and ```item``` as arguments. ```box_name``` states the name of the box inside the grid, namely "1", "2", "3" and etc. ```item``` is the product to be showed in the grid box. The content of the ```item``` is passed from "page_content.js" by fetching the API "page_content". The function creates and updates the content of the grid box. 

```
function item_box_content_empty(box_name){ 
    ...
}
```
The function takes ```box_name``` as argument. It is the same as the one in previous function "item_box_content". There are total of 9 grid boxes per page. If the no. of prodct showed in the current page is less not 9, then some grid box are empty. The function are used to convert the grid box into empty grid box.

#### mouseover_effect.js :

It is a javascript file which contains the functions for mouserover effect when the mouse move over the product grid box inside the index page and search result page.

```
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('mouseover', event => {
        ...
    });
})
```

When the mouse is moved to grid box, the "opacity" will be changed to 0.5, it indicates the user is selecting the product.

```
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('mouseout', event => {
        ...
    })
})
```
When the mouse is moved out from grid box, the "opacity" will be changed to 1, it resets opacity and indicates the user is selecting nothing.

#### page_content.js :

It is a javascript file which contains the functions for loading the products information for different page no. by the page navigator in the index page.

```
function load_grid_items(page_no, category_id){
    ...
}
```

The function take ```page_no``` and ```category_id``` as arguments. The ```page_no``` is the page no. that passed from "page_navigator.js". The ```category_id``` is the category id of the product. The function fetched the API "```/page_content/${page_no}/${category_id}```" to get the details of the product and then passing the result to ```item_box_content(box_name, item)```.

#### page_content(search).js :

It is a javascript file which contains the functions for loading the products information for different page no. by the page navigator in the search result page.

```
function load_grid_items_search(page_no, search_text) {
    ...
}
```
The function takes ```page_no``` and ```search_text``` as arguments. The argument ```page_no``` just like the one in ```load_grid_items(page_no, category_id)```, is the page no. that passed from "paga_navigator(search).js". The ```search_text``` is the string from search function from index page. The function fetches the API "```/search_page_content/${page_no}/${search_text}```" to get the details of the product and then passing the result to ```item_box_content(box_name, item)```.

#### page_navigator.js :

It is a javascript file which contains the functions for navigating pages inside the index page.

```
function page_navigator(current_page, category_id){
    ...
}
```
The function takes ```current_page``` and ```category_id``` as arguments. The argument ```current_page``` indicates the currnet page no. of content inside the index page. Argument ```category_id``` is the category id of the product. The function creats the page navigation button. Based which button is pressed, the function calls ```load_grid_items(page_no, category_id)``` to update the page content.

#### page_navigator(search).js :

It is a javascript file which contains the functions for navigating pages inside the search result page.

```
function page_navigator_search(current_page, search_text){
    ...
}
```
The function takes ```current_page``` and ```search_text``` as arguments. The argument ```current_page``` indicates the currnet page no. of content inside the index page. Argument ```search_text``` is the string from search function from index page. The function creats the page navigation button in search_result page. Based which button is pressed, the function calls ```load_grid_items_search(page_no, search_text)``` to update the page content.

#### quantity_add_sub.js :

It is a javascript file which contains the function for creating a "add" and "sub" button to increase and decrease the no. of qunatity box.

```
function quantity_add(target){
    ...
};

function quantity_sub(target){
    ...
};
```

The functions take ```target``` as argument. ```target``` is the class name of the quantity box. The functions increase or decrease the value inside the quantity box.

#### style.css :

It is a CSS file which contains the CSS for the html files. 

#### Folder "images" :

 It is a folder to store the product images which is uploaded by the shop owner(superuser).

### Folder "capstone/eshopping/templates/eshopping/"

#### detail.html :

It is a html file for showing the product detial when the user has clicked the product in the index page. User can add the product to the shopping cart. User can click the image with the class ```small_image``` it swapes with the ```large_image```

#### index.html :

It is index page of the web application. The page shows all the products which are selling. User can also use filter the product by cateogry and also search the product by keywords. User can click one of the product and it redirects to detail.html. User can press the page link to switch the pages.  

#### layout.html :

It is layout html file which set the layout for other html file. The layout contain the hyper link to "login", "register", "logout", "profile", "shopping cart" and "for staff". 

#### login.html :

It a html file for user to login.

#### order_manage.html: 

It a html file for shop owner to do order managment. All the orders information will be displayed in this page. Owner can update the order information here.

#### profile.html: 

It a html file for showing the personal information and order history of the requested user.

#### protected_view.html: 

It is a html file for showing error message that this page can be accessed with staff account only.

#### register.html : 

It is a html file for user to register account.

#### search_result.html :

It is a html file for showing the search_result after user has input the search keywords. User can click one of product and then it will redirect the detail.html. User can press page link to swithc different page.  

#### shopping_cart.html: 

It is a html file for showing the shopping cart of the user. User can edit the shopping cart. Use can confirm the order by pressing the "place order" button. 

#### staff_view.html :

It is a html file for staff account only. Staff can go to order managment and stock managment in this page.

#### stock_manage.html :

It is a html file for shop owner to do stock managment. Owner can view the stock detail. Owner can also update the stock. 

### Folder "capstone/eshopping/"

#### admin.py : 

It is a python file for registering all the models to the Django admin site.

#### models.py:

It is a python file for creating the models used in this application.

* ```class User(AbstractUser):``` : It is a database model for storing user details.

* ```class Category(models.Model):``` : It is a database model for storing the list of category.

* ```class Item(models.Model):``` : It is a database model for storing the details of the products.

* ```class ProductImage(models.Model):``` : It is a database model for storing the product images.

* ```class ShoppingCart(models.Model):``` : It is a database model for storing the shopping cart details.

* ```class OrderStatus(models.Model):``` : It is a database model for storing the list of order status.

* ```class PlacedOrder(models.Model):``` : It is a database model for storing the details of the order. 

#### urls.py: 

It is a python file for storing all the urls (including API) which used in this application.

* ```path("", views.index, name='index')``` : The route is for index view.

* ```path("login", views.login_view, name="login")``` : The route is for login view.

* ```path("logout", views.logout_view, name="logout")``` : The route is for logout view.

* ```path("register", views.register, name="register")``` : The route is for register view.

* ```path("item_detail/<int:id>", views.item_detail, name="item_detail")``` : The route is for item_detail view which takes item id, ```id```, as argument.

* ```path("item_search", views.item_search, name="item_search")``` : The route is for item_search view.

* ```path("view_shopping_cart", views.view_shopping_cart, name="view_shopping_cart")``` : The route is for view_shopping_cart view.

* ```path("placing_order", views.placing_order, name="placing_order")``` : The route is for placing_order view.

* ```path("user_profile", views.user_profile, name="user_profile")``` : The route is for user_profile view.

* ```path("staff_view", views.staff_view, name="staff_view")``` : The route is for staff_view view.

* ```path("protected_view", views.protected_view, name="protected_view")``` : The route is for protected_view view.

* ```path("order_manage", views.order_manage, name="order_manage")``` : The route is for order_manage view.

* ```path("customer_detail/<int:user_id>", views.customer_detail, name="customer_detail")``` : The route is for customer_detail view which takes the user id, ```user_id```, as argument. 

* ```path("stock_manage", views.stock_manage, name="stock_manage")``` : The route is for stock_manage view.

* ```path("page_content/<int:page_no>/<int:category_id>", views.page_content, name="page_content")``` : This is a API route for page_content view which takes the page no., ```page_no```, and category id, ```category_id```, as arguments.

* ```path("total_page_no_filter/<int:category_id>", views.total_page_no_filter, name="total_page_no_filter")``` : This is a API route for total_page_no_filter view which takes the category id, ```category_id``` as argument.

* ```path("search_page_content/<int:page_no>/<str:search_text>", views.search_page_content, name="search_page_content")``` : This is a API route for search_page_content view which takes page no., ```page_no```, and search keyword, ```search_text```, as arguments.

* ```path("add_shopping_cart/<int:item_id>", views.add_shopping_cart, name="add_shopping_cart")``` : This is a API route for add_shopping_cart view which takes item id, ```item_id``` as argument. 

* ```path("edit_shopping_cart_item_no/<int:item_id>", views.edit_shopping_cart_item_no, name="edit_shopping_cart_item_no")``` : This is a API route for edit_shopping_cart_item_no view which takes item id, ```item_id```, as argument. 

* ```path("stock_check/<int:item_id>", views.stock_check, name="stock_check")``` : This is a API route for stock_check view which takes item id, ```item_id```, as argument.

* ```path("order_detail/<int:order_id>", views.order_detail, name="order_detail")``` : This is a API route for order_detail view which takes order id, ```order_id```, as argument.

#### util.py :

It is a python file for storing some variables and functions which used in this application.

* ```no_item_per_page = 9``` : It define how many product are shown on each page.

* ```def check_exist_shopping_cart(user, item):``` : It checks whether shopping cart has certain item inside or not. 


#### views.py : 

It is a python file which includes all the views which used in this application.

* ```def login_view(request):``` : It is a view for login. If the request method is "POST". It checks if the username and password are correct. If yes, then the user is authenticated. If not, it returns error message. If the request method is not "POST", then it redirects to "login.html".

* ```def logout_view(request):``` : It is a view for logout. The user is logout and return to index view.

* ```def register(request):``` : It is a view for register. If the request method is "POST", it checks if the username is already exist and the password is dobule confirmed. If yes, it register the user to the ```User``` model and then login. If not, it returns error message. If the request method is not "POST", it redirects to "register.html".

* ```def index(request):``` : It is a view for index page. It renders the page "index.html" with the category list ```categories``` and other variables for page navigating. 

* ```def page_content(request, page_no, category_id):``` : It is a API view for returning product details with certain page no and category. 

* ```def total_page_no_filter(request, category_id):``` : It is a API view for returning the total no. of page for the page navigation with certain category. 

* ```def item_search(request):``` : It is a view for item search. The search keyword is passed from the form and get the product details by the keyword. And then it renders the "search_result.html".

* ```def item_detail(request, id):``` : It is a view for showing item detail. It renders the "detail.html" with certain item id.

* ```def search_page_content(request, page_no, search_text):``` : It is a API view for returning the product detail by search keyword.

* ```def add_shopping_cart(request, item_id):``` : It is API view for adding item into the shopping cart. If the request method is "POST", the view gets the item id and quantity and update the ```ShoppingCart``` model.

* ```def view_shopping_cart(request):``` : It is a view for viewing the shopping cart. It renders the "shopping_cart.html" with the shopping cart detail. 

* ```def edit_shopping_cart_item_no(request, item_id):``` : It is a API view for returning cart detail and updating the cart. If request method is "GET", the view returns the quantity for certain item inside the shopping cart. If request method is "POST":, it updates the quantity for certain item or remove the item inside the shopping cart.

* ```def placing_order(request):``` : It is a view for placing order. It gets the detail from the ```ShoppingCart``` for request user and update the ```PlacedOrder``` model. After updating the ```PlacedOrder``` model, the details inside ```ShoppingCart``` is deleted. 

* ```def user_profile(request):``` : It is a view for viewing the user profile. It renders the "profile.html" with user detail.

* ```def stock_check(request, item_id):``` : It is API route for returning and updating the item stock. If the request method is "GET", it returns the no. of stock of item with item id ```item_id```. If the request method is "POST", it updates the no. stock of item with item id ```item_id```.

* ```def staff_view(request):``` : It is view for staff view page. It renders the "staff_view.html".

* ```def protected_view(request):``` : It is view for staff view protection. When non staff account accesses the staff only view, it renders the "protected_view.html". 

* ```def order_manage(request):``` : It is view for order management. It renders the "order_manage.html" with the order detail.

* ```def order_detail(request, order_id):``` : It is API view for returning and updating the order detail. If the request method is "GET", it returns the order detail with order id ```order_id```. If the request method is "POST", it updates the ```PlacedOrder``` model. 

* ```def customer_detail(request, user_id):``` : It is a view for staff account to view other user profile. It renders the "profile.html" with certain user id ```user_id```.

* ```def stock_manage(request):``` : It is a view for stock management. It renders the "stock_manage.html" with the stock detail. 

#### requirements.txt :

It is txt file which states what packages/modules are needed to run this application.

## To run the application
To run the application, move to the main directory of this project "capstone" inside the terminal. Type "python manage.py runserver" and press enter. An http address "http://127.0.0.1:8000/" will be shown in the terminal. Press the address and the web browser will be opened. The index page will be shown. The application is running. 

A superuser has been created in advance. 

Username: super

Password : MSN00100

the superuser is also a staff account which it can access the staff only features (order and stock managment).

If the user want to add more products, edit product details or add more category type, please visit the admin site "http://127.0.0.1:8000/admin". Please login with the superuser account. 