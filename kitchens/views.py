from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from kitchens.models import *

# Create your views here.
def dashboard(request):
    context = {
        'allKitchens': Kitchen.objects.all(),
        'allOrders': Order.objects.all(),
    }
    return render(request, 'dashboard.html', context)

def add_kitchen(request):
    errors = Kitchen.objects.kitchen_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:

        kitchen = Kitchen.objects.create(
            name=request.POST['kitchen_name'],
            designation_id=request.POST['designationId']
            )
    return redirect("/")

def add_order(request):    
    # errors = Order.objects.order_validator(request.POST)

    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    # else:
    kitchen = Kitchen.objects.get(id=request.POST['kitchen_id'])
    dateFormatted = datetime.datetime.today().strftime("%Y%m%d")
    count =  kitchen.daily_order_count + 1
    orderNum = f"{kitchen.designation_id}-{dateFormatted}-{count}"
    notes = request.POST['notes']
    status = "in progress"


    Order.objects.create(
        order_num=orderNum, 
        kitchen=kitchen,
        notes = notes,
        status = status
        )

    kitchen.daily_order_count += 1
    kitchen.save()

    return redirect('/')

def kitchenDashboard(request, kitchen_id):
    context = {
        'kitchen': Kitchen.objects.get(id=kitchen_id)
    }
    return render(request, 'kitchenDashboard.html', context)

def update_order_status(request, order_id):
    statuses = ["in progress", "ready", "done"]
    
    order = Order.objects.get(id=order_id)
    currentStatus = order.status.lower()

    if statuses.index(currentStatus) + 1 == len(statuses):
        nextStatus = 0
    else:
        nextStatus = statuses.index(currentStatus) + 1
    order.status = statuses[nextStatus]
    order.save()
    return redirect('/')

def all_orders(request):
    context = {
        'allOrders': Order.objects.all()
    }
    return render(request, 'allOrders.html', context)

def display_screen(request):
    context = {
        'allOrders': Order.objects.all()
    }
    return render(request, 'displayScreen.html', context)