"""
URL configuration for budgetapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import budget_view, home_view, account_info_view, expense_info_view
from .api import AccountInfoAPIView

urlpatterns = [
    path('', home_view, name='home'),
    path('budget/', budget_view, name='budget'),
    path('account-info/', account_info_view, name='account-info'),
    path('expense-info/', expense_info_view, name='expense-info'),
    path('api/accountinfo/', AccountInfoAPIView.as_view(), name='api-account-info')
]


