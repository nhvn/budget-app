from rest_framework import generics
from .models import AccountInfo
from .serializers import AccountInfoSerializer

class AccountInfoAPIView(generics.ListCreateAPIView):
    queryset = AccountInfo.objects.all()
    serializer_class = AccountInfoSerializer
