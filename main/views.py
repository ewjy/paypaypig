from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests

# Create your views here.
def main(request):
    return render(request, 'index.html')
def bank(request):
    return render(request, 'bank-sel.html')
def pay(request):
    if request.method == "POST":
        print("POST get!")
        print(request.POST['tsib'])
    return render(request, 'pay-sel.html')
def merchant(request):
    if request.method == "POST":
        print("POST get!")
        print(request.POST['line_pay'])
    return render(request, 'merchant.html')    
def results(request):
    return render(request, 'results.html')