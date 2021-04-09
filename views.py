from django.shortcuts import render
from .models import *

# Create your views here.
def dashboard(request):

    order_tenant = {}
    order_landlord = {}

    customer = request.user.customer

    try:
        t = Tenant.objects.get(user=customer)
        order_tenant = Order.objects.filter(tenant=t)
        l = order_tenant.landlord
    except:
        print("Not a tenant")
    
    try:
        l = Landlord.objects.get(user=customer)
        order_landlord = Order.objects.filter(tenant=t)
        t = order_tenant.tenant
    except:
        print("Not a landlord")
    
    print(order_tenant, order_landlord)

    context = {"order_tenant":order_tenant}
    return render(request, 'escrow/dashboard.html', context)

def checklist(request):

    context = {}
    return render(request, 'escrow/checklist.html', context)

def trip(request):
    context = {}
    return render(request, 'escrow/trip.html', context)

def upload(request):
    
    context = {}
    return render(request, 'escrow/upload.html', context)
