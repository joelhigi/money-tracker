from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'moneymanager/index.html')
def add_expense(request):
    return render(request, 'moneymanager/add-expense.html')