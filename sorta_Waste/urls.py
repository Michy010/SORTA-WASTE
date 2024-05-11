from django.urls import path
# from .views import update_location
from . import views

app_name = 'sorta_Waste'
urlpatterns = [
    path('', views.index, name= 'home'),
    path('update-location/', views.update_location, name='update_location'),
    path('waste_order_page/', views.waste_order_page, name='orders'),
    path('order_list/', views.order_list, name='order_list_page'),

]
