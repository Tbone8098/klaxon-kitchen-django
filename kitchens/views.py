from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .filters import OrderFilter
from kitchens.models import *
from login.models import *
import datetime
import csv

# Create your views here.
def dashboard(request):
    allKitchens = Kitchen.objects.all()
    allOrders = Order.objects.order_by("-id").all()

    myFilter = OrderFilter(request.GET, queryset=allOrders)
    allOrders = myFilter.qs

    context = {
        'allKitchens': allKitchens,
        'allOrders': allOrders,
        'myFilter': myFilter
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
            designation_id=request.POST['designationId'].upper()
            )
    return redirect('klaxonKitchen:home')

def add_order(request):  
    errors = Order.objects.Order_validator(request.POST)  

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        kitchen = Kitchen.objects.get(id=request.POST['kitchen_id'])
        dateFormatted = datetime.datetime.today().strftime("%Y%m%d")
        count =  kitchen.daily_order_count + 1
        ticketNum = f"{kitchen.designation_id}-{dateFormatted}-{count}"
        orderNum = request.POST['orderNum']
        notes = request.POST['notes']
        status = "in progress"


        Order.objects.create(
            ticket_num=ticketNum,
            order_num=orderNum, 
            kitchen=kitchen,
            notes = notes,
            status = status
            )

        kitchen.daily_order_count += 1
        kitchen.save()

    return redirect('klaxonKitchen:home')

def kitchenDashboard(request, kitchen_id):
    kitchen = Kitchen.objects.order_by("-id").get(id=kitchen_id)
    allOrders = Order.objects.order_by("-id").all()

    context = {
        'kitchen': kitchen,
        'allOrders': allOrders
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
    return redirect('klaxonKitchen:home')

def all_orders(request):
    all_orders = Order.objects.order_by('-id').all()

    myFilter = OrderFilter(request.GET, queryset=all_orders)
    all_orders = myFilter.qs

    context = {
        'allOrders': all_orders,
        'myFilter': myFilter
    }
    return render(request, 'allOrders.html', context)

def display_screen(request):
    context = {
        'allOrders': Order.objects.all()
    }
    return render(request, 'displayScreen.html', context)

def export_orders(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['order_num', 'notes', 'status', 'kitchen', 'created_at', 'updated_at'])

    all_orders = Order.objects.order_by('-id').all()
    # myFilter = OrderFilter(request.GET, queryset=all_orders)
    # all_orders = myFilter.qs

    for order in all_orders.values_list('order_num', 'notes', 'status', 'kitchen', 'created_at', 'updated_at'):
        writer.writerow(order)

    response['Content-Disposition'] = 'attachment; filename="Orders.csv"'

    return response
    # return HttpResponse(all_orders)

def export_kitchens(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['name', 'designation_id', 'daily_counter', 'created_at', 'updated_at'])

    for kitchen in Kitchen.objects.all().values_list('name', 'designation_id', 'daily_order_count', 'created_at', 'updated_at'):
        writer.writerow(kitchen)

    response['Content-Disposition'] = 'attachment; filename="Kitchens.csv"'

    return response

def deleteOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()

    return redirect('klaxonKitchen:all_orders')

def deleteOrderConfirm(request, order_id):
    context = {
        'order_id': order_id
    }
    return render(request, 'confirmOrderDelete.html', context)

def reset_counter_all(request):
    all_kitchens = Kitchen.objects.all()
    for kitchen in all_kitchens:
        kitchen.daily_order_count = 0
        kitchen.save()
    return redirect('klaxonKitchen:home')

def settings(request):
    return render(request, 'settings.html')

def kitchenDelete(request, kitchen_id):
    kitchen = Kitchen.objects.get(id=kitchen_id)
    kitchen.delete()
    return redirect('klaxonKitchen:home')

def kitchenDeleteConfirm(request, kitchen_id):
    context = {
        'kitchen_id': kitchen_id
    }
    return render(request, 'confirmKitchenDelete.html', context)

def order_details(request, order_id):
    current_order = Order.objects.get(id=order_id)
    allKitchens = Kitchen.objects.all()
    context = {
        'currentOrder': current_order,
        'allKitchens': allKitchens
    }
    return render(request, 'orderDetails.html', context)

def order_update(request, order_id):
    orderNum = request.POST['orderNum']
    kitchen = request.POST['kitchen']
    notes = request.POST['notes']

    linkedKitchen = Kitchen.objects.get(id=kitchen)

    orderToUpdate = Order.objects.get(id=order_id)

    orderToUpdate.order_num = orderNum
    orderToUpdate.kitchen = linkedKitchen
    orderToUpdate.notes = notes

    orderToUpdate.save()

    return redirect(f'/klaxonKitchenorder_details/{order_id}')