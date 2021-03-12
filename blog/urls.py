from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.blog,name="bloghome"),
    path("blogpost/<int:ids>",views.blogpost,name="blogpost"),
]