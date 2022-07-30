from random import randint
from multiprocessing import context
from statistics import quantiles
from urllib import request

from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages


from .models import Cuisine,Food,Order

def menu(request):
   
    foods=Food.objects.all()
    context={
        # 'cuisine':cuisine
        'foods':foods
    }
    return render(request, 'food/menu.html',context)

def details(request, id):
    food = Food.objects.get(id=id)
   
    context={
        'food':food
       
    }
    return render(request, 'food/details.html', context)

def add_to_cart(request):
    if request.method=="POST":
        food_id=request.POST.get("food_id")
        quantity=request.POST.get("quantity")
        food_items={}
        if request.session.get("food_items"):
            food_items=request.session.get("food_items")
        food_items[food_id]=quantity
        request.session["food_items"]=food_items
        print( request.session["food_items"])
    return redirect('cart')
def cart(request):
    food_items=request.session.get("food_items")
    items=[]
    total_price=0
    if food_items:
        for id,quantity in food_items.items():
            food=Food.objects.get(id=id)
            price=int(quantity) * int(food.price)
            total_price +=price
            items.append({
                "id":id,
                "name":food.name,
                "quantity":quantity,
                "price":price,
                "photo":food.image
            })
    context={
        "foods":items,
        "total_price":total_price
    }
    return render(request,'food/cart.html',context)
def delete_cart_item(request,id):
    food_items=request.session.get("food_items")
    del food_items[id]
    request.session["food_items"]=food_items
    return redirect('cart')

def check_out(request):
    if not request.session.get("OTP"):
        otp=randint(111111,999999)
        send_mail(
            "OTP from sit cafe",
            f"your otp to order food from sit cafe is {otp}",
            "tusharkantanayak713@gmail.com",
            [request.user.email,],
            fail_silently=False
        )
        request.session["OTP"]=otp
    return render(request,'food/check_out.html')
def place_order(request):
    if request.method=="POST":
        otp=request.POST.get("otp")
        if request.session.get("OTP") != int(otp):
            messages.error(request,"INVALID OTP")
            return redirect("check_out")
        else:
            foods=request.session.get("food_items")
            if foods:
                order_details=""
                total_price=0
                for id,quantity in foods.items():
                    food=Food.objects.get(id=id)
                    price=food.price *int(quantity)
                    total_price +=price
                    order_details += f"{food.name} x {quantity}"
                order = Order(user=request.user , order_details=order_details,total_price=total_price)
                order.save()
                del request.session["food_items"]
                del request.session["OTP"]


    return redirect('orders')

def orders(request):
    orders=Order.objects.filter(user=request.user)
    context={
        "orders":orders
    }
    return render(request,'food/orders.html',context)
