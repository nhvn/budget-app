from django.http import HttpResponse
from django.shortcuts import render
from .models import AccountInfo, ExpenseInfo

def budget_view(request):
    budget_items = AccountInfo.objects.all()  # fetch data from AccountInfo model
    return render(request, 'budget.html', {'budget_items': budget_items})

def home_view(request):
    return HttpResponse("Welcome to the budget app!")

def account_info_view(request):
    account_info = AccountInfo.objects.all()
    return HttpResponse(account_info)

def expense_info_view(request):
    expense_info = ExpenseInfo.objects.all()
    return HttpResponse(expense_info)

