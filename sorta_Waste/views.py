from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'sorta_waste/index.html') 

def producer (request):
    return render (request, 'sorta_waste/producer.html') 

def collector (request):
    return render (request, 'sorta_waste/collector.html') 


