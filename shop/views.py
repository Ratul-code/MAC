from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product,Contact,Order,OrderUpdate
import math
import json

# Create your views here.
def shop(request):

    allprods=[]

    category_id=product.objects.values('Category',"id")

    categories={item["Category"] for item in category_id}

    for catprod in categories:

        prod=product.objects.filter(Category=catprod)

        n=len(prod)

        nslides=math.ceil(n/4)

        allprods.append([prod,range(1,nslides),nslides])

    param={'allprods':allprods}

    return render(request,'home.html',param)











def prodview(request,myid):

    Product=product.objects.filter(id=myid)

    return render(request,'pordview.html',{'product':Product[0]})











def checkout(request):

    if request.method=='POST':

        item_json=request.POST.get('itemsJson','')

        name=request.POST.get('name','')

        email=request.POST.get('email','')

        address=request.POST.get('address','') +request.POST.get('address2','') 

        city=request.POST.get('city','')

        state=request.POST.get('state','')

        zip_code=request.POST.get('zip_code','')

        phone=request.POST.get('phone','')

        od=request.POST.get('id','')

        order=Order(item_json=item_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)

        order.save()

        thank=True

        update=OrderUpdate(order_id=order.order_id,update_desc="The Order has been placed.")
        update.save()
        id=order.order_id
        return render(request,'checkout.html',{"thank":thank,"id":id})
    return render(request,'checkout.html')











def tracker(request):
    if request.method=='POST':
        order_id=request.POST.get('id','')

        email=request.POST.get('email','')

        try:
            order=Order.objects.filter(order_id=order_id,email=email)
            if len(order)==1:
                update=OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps(updates , default=str)
                return HttpResponse(response)
            else:
                return HttpResponse({"{}"})
        except Exception as e:
            return HttpResponse("{}")
    return render(request,'tracker.html')








































def contact(request):

    if request.method=='POST':

        name=request.POST.get('name','')

        email=request.POST.get('email','')

        phone=request.POST.get('phone','')

        desc=request.POST.get('message','')

        contact=Contact(Name=name,Email=email,Phone=phone,Description=desc)

        contact.save()

        thank=True

        return render(request,'contact.html',{'thank':thank})

    return render(request,'contact.html')
























def about(request):

    return render(request,'about.html')
