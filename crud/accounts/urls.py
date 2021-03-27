from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('product',views.product,name="product"),
    path('customer/<str:pk>/',views.customer,name="customer"),
]