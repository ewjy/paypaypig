from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name = "main"),
    path('bank/', views.bank, name = "bank"),
    path('pay/', views.pay, name = "pay"),
    path('merchant/', views.merchant, name = "merchant"),
    path('results/', views.results, name = "results"),
    path('result1/', views.result1, name = "result1"),
    path('result2/', views.result2, name = "result2"),
    
]