
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("all_post", views.all_post, name="all_post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("unfollow/<int:user_id>", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),

    # API Routes
    path("edit/<int:id>", views.edit, name="edit"),
    path("like/<int:id>", views.like_post, name="like"),
    path("unlike/<int:id>", views.unlike_post, name="unlike")
]
