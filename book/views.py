from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
  # 추가한 권한을 가져옵니다.

from .serializers import *
from .models import *

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 현재 인증된 사용자를 user 필드에 할당합니다.
# Create your views here.
