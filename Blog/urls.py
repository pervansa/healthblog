from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # path("", views.index, name="index"),
    path("home/", views.home, name="Home page"),
    path("contact/", views.contact, name="contact me"),
    path("about/", views.about, name="about me"),
    path("healthcare/", views.healthcare, name="Health blog"),
    path("hippa/", views.hippa, name="hippa"),
    path("", views.home, name="Main page"),
    path("search/", views.search, name="Search"),
    path("signup", views.handlesignup, name="handlesignup"),
    path("login", views.handlelogin, name="handlelogin"), 
    path("logout", views.handlelogout, name="handlelogout")



    # path("blog/", views.blog, name="home page"),
    # path('<str:slug>' views.home, name ="blog post")
]
