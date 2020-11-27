from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.shop,name="shopapp"),
    path("shop1",views.shop1,name="extrahome"),
    path("about",views.about,name="about"),
]