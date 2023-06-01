from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ExpenseInfo
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView

def budget_view(request):
    budget_items = User.objects.all()  # fetch data from User model
    return render(request, 'budget.html', {'budget_items': budget_items})

def home_view(request):
    return HttpResponse("Welcome to the budget app!")

def expense_info_view(request):
    expense_info = ExpenseInfo.objects.all()
    data = list(expense_info.values())  # Convert to a list of dictionaries
    return JsonResponse(data, safe=False)  # Return the data as JSON

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        print(request.body)  # Print the raw request body
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            response = super().form_valid(form)
            user = self.object
            data = {
                "username": user.username,
                "email": user.email,
            }
            return JsonResponse(data)
        else:
            print(form.errors)
            return super().form_invalid(form)

    def form_invalid(self, form):
        # Collect form.errors into a dict
        errors = {field: errors for field, errors in form.errors.items()}
        return JsonResponse(errors, status=400)

class LoginView(LoginView):
    template_name = 'login.html'

