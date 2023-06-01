from rest_framework import generics
from .models import ExpenseInfo
from .serializers import ExpenseInfoSerializer

class ExpenseInfoAPIView(generics.ListCreateAPIView):
    queryset = ExpenseInfo.objects.all()
    serializer_class = ExpenseInfoSerializer
