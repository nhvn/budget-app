from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# ExpenseInfo model
class ExpenseInfo(models.Model):
    expense_name = models.CharField(max_length=20)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    expense_category = models.CharField(max_length=20)
    expense_description = models.TextField()
    expense_location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship

    created_at = models.DateTimeField(default=timezone.now)  # Timestamps
    updated_at = models.DateTimeField(auto_now=True)  # Timestamps

    def __str__(self):
        return self.expense_name

    def clean(self):
        # Custom validation: Expense amount must be positive
        if self.expense_amount <= 0:
            raise ValidationError("Expense amount must be positive.")
