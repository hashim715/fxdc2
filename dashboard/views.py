from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'dashboard.html')

def deposit(request):
	return render(request, 'deposit.html')

def withdraw(request):
	return render(request, 'withdraw.html')

def transfer(request):
	return render(request, 'transfer.html')