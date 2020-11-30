from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product,Contact
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


def prodview(request,myid):
    # fetching bny id
    Product=product.objects.filter(id=myid)
    # print(Product)

    return render(request,'pordview.html',{'product':Product[0]})


def tracker(request):
    return render(request,'tracker.html')


def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('message','')
        contact=Contact(Name=name,Email=email,Phone=phone,Description=desc)
        contact.save()
    return render(request,'contact.html')

def contacts(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('message','')
        contact=Contact(Name=name,Email=email,Phone=phone,Description=desc)
        contact.save()
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')