from rest_framework import serializers
from .models import ExpenseInfo

class ExpenseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseInfo
        fields = '__all__'
