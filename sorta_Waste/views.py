from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from . forms import WasteOrderForm
from . models import WasteOrder
from django.http import JsonResponse

# Create your views here.

def index (request):
    return render (request, 'sorta_waste/index.html') 

    

def collector (request):
    return render (request, 'sorta_waste/collector.html') 


def update_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        if latitude and longitude:
            # Store latitude and longitude in user's profile or session
            return JsonResponse({'message': 'Location updated successfully.'})
        else:
            return JsonResponse({'error': 'Latitude and longitude are required.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def waste_order_page (request):
    if request.method == 'POST':
        form = WasteOrderForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('sorta_Waste:order_list_page')
        
    else:
        form = WasteOrderForm ()
    
    return render (request, 'sorta_Waste/waste_order_page.html', {'form':form} )

def order_list (request):
    orders = WasteOrder.objects.all()
    # quantities = WasteAmount.objects.all()
    return render (request, 'sorta_Waste/order_list.html', {'orders':orders})