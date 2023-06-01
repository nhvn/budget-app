from django.urls import path, include  # include is added here
from .views import budget_view, home_view, expense_info_view, SignUpView, LoginView
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('budget/', budget_view, name='budget'),
    path('', home_view, name='home'),
    path('expense/', expense_info_view, name='expense'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # include is used here
]
