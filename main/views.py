from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import UserForm
from .models import user
# Create your views here.
def main(request):
    return render(request, 'index.html')
def bank(request):
    return render(request, 'bank-sel.html')
def pay(request):
    return render(request, 'pay-sel.html')
def merchant(request):
    return render(request, 'merchant.html')    
def results(request):
        return render(request, 'result1.html')
def result1(request):
        return render(request, 'result1.html')   
def result2(request):
        return render(request, 'result1.html')
def result3(request):
        return render(request, 'result1.html')
def result4(request):
        return render(request, 'result1.html')
def result5(request):
        return render(request, 'result1.html')
def result6(request):
        return render(request, 'result1.html')
def result7(request):
        return render(request, 'result1.html')
def postBank(request):
    if request.is_ajax and request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error":""}, status=400)
