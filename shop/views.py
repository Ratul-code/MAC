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

    return render(request,'shop/home.html',param)


def srmc(query,item):
    if query in item.Name.lower() or query in item.Description.lower()  or query in item.Category.lower()  or query in item.Subcategory.lower() or query in item.Name or query in item.Description  or query in item.Category  or query in item.Subcategory :
        return True
    else:
        return False


def search(request):

    query=str(request.GET.get('search'))
    print(query)

    allprods=[]

    category_id=product.objects.values('Category')

    categories={item["Category"] for item in category_id}

    for catprod in categories:

        prods=product.objects.filter(Category=catprod)

        prod=[item for item in prods if srmc(query , item)]

        n=len(prod)

        nslides=math.ceil(n/4)

        if len(prod) != 0 and len(query) > 2:

            allprods.append([prod,range(1,nslides),nslides])

    param={'allprods':allprods,'msg':""}

    if len(prod)==0 or len(query) < 2:

        param={'msg':"Please , Make sure to search relevant queries"}


    return render(request,'shop/search.html',param)











def prodview(request,myid):

    Product=product.objects.filter(id=myid)

    return render(request,'shop/pordview.html',{'product':Product[0]})











def checkout(request):

    if request.method=='POST':

        item_json=request.POST.get('itemsJson','')

        amount=request.POST.get('amount','')

        name=request.POST.get('name','')

        email=request.POST.get('email','')

        address=request.POST.get('address','') +request.POST.get('address2','') 

        city=request.POST.get('city','')

        state=request.POST.get('state','')

        zip_code=request.POST.get('zip_code','')

        phone=request.POST.get('phone','')

        od=request.POST.get('id','')

        order=Order(item_json=item_json,amount=amount,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)

        order.save()

        thank=True

        update=OrderUpdate(order_id=order.order_id,update_desc="The Order has been placed.")
        update.save()
        id=order.order_id
        return render(request,'shop/checkout.html',{"thank":thank,"id":id})
    return render(request,'shop/checkout.html')











def tracker(request):
    if request.method=='POST':
        order_id=request.POST.get('id','')

        email=request.POST.get('email','')

        try:
            order=Order.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].item_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse({"{}"})
        except Exception as e:
            return HttpResponse("{}")
    return render(request,'shop/tracker.html')








































def contact(request):

    if request.method=='POST':

        name=request.POST.get('name','')

        email=request.POST.get('email','')

        phone=request.POST.get('phone','')

        desc=request.POST.get('message','')

        contact=Contact(Name=name,Email=email,Phone=phone,Description=desc)

        contact.save()

        thank=True

        return render(request,'shop/contact.html',{'thank':thank})

    return render(request,'shop/contact.html')
























def about(request):

    return render(request,'shop/about.html')
