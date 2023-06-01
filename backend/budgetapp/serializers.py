from rest_framework import serializers
from .models import AccountInfo

class AccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInfo
        fields = '__all__'
