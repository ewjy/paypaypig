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
    path('result3/', views.result3, name = "result3"),
    path('result4/', views.result4, name = "result4"),
    path('result5/', views.result5, name = "result5"),
    path('result6/', views.result6, name = "result6"),
    path('result7/', views.result7, name = "result7"),
]