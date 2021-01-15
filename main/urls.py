from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name = "main"),
    path('bank/', views.bank, name = "bank"),
    path('pay/', views.pay, name = "pay"),
    path('merchant/', views.merchant, name = "merchant"),
]