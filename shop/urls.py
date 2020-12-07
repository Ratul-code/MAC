from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.shop,name="shopapp"),
    path("about",views.about,name="about"),
    path("tracker",views.tracker,name="tracker"),
    path("contact",views.contact,name="contact"),
    path("product/<int:myid>",views.prodview,name="product"),
    path("checkout",views.checkout,name="checkout"),
]