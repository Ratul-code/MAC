from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product
import math

# Create your views here.
def shop(request):
    allprods=[]
    category=product.objects.values('Category','id')
    catprod={item["Category"] for item in category}
    for cat in catprod:
        prod=product.objects.filter(Category=cat)
        n=len(prod)
        nslides=math.ceil(n/4)
        allprods.append([prod,range(1,nslides),nslides])
    param={'allprods':allprods}
    return render(request,'home.html',param)


def shop1(request):
    return render(request,'backup.html')


def about(request):
    return render(request,'about.html')