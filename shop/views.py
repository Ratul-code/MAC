from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product
import math

# Create your views here.
def shop(request):
    products=product.objects.all()
    n=len(products)
    nslides=math.ceil(n/4)

    allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]

    param={'allprods':allprods,'nslides':range(1,nslides)}
    return render(request,'home.html',param)


def shop1(request):
    return render(request,'backup.html')


def about(request):
    return render(request,'about.html')