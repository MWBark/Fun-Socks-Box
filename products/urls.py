from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/images', views.images, name='images'),
    path('<int:product_id>/images/add', views.add_image, name='add_image'),
    path('<int:product_id>/images/delete/<int:image_id>', views.delete_image, name='delete_image'),
]
