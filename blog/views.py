from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
import random

# Create your views here.
def blog(request):
    blog=Blogpost.objects.all() 
    return render(request,"blog/home.html",{"blog":blog})


def blogpost(request,ids):
    blogpost=Blogpost.objects.filter(post_id=ids)[0]
    randblog=random.choice(Blogpost.objects.all())
    return render(request,"blog/blogpost.html",{"post":blogpost,"sug":randblog})