from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addresses/', views.addresses, name='addresses'),
    path('addresses/add/', views.add_address, name='add_address'),
    path('addresses/update/<int:address_id>/',
         views.update_address, name='update_address'),
    path('addresses/delete/<int:address_id>/',
         views.delete_address, name='delete_address'),
    path('addresses/default/<int:address_id>/',
         views.set_default, name='set_default'),
]
