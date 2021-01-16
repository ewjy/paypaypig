from django.shortcuts import render

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
    return render(request, 'results.html')