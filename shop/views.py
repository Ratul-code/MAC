from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product
import math

# Create your views here.
def shop(request):
    products=product.objects.all()
    n=len(products)
    nslides=math.ceil(n/4)
    param={'product':products,'no_of_slides':nslides,
    'range':range(1,nslides)}
    return render(request,'home.html',param)
def shop1(request):
    return render(request,'home1.html')
def about(request):
    return render(request,'about.html')