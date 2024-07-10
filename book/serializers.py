from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')  # user 필드를 읽기 전용으로 설정합니다.
    class Meta:
        model : Book
        field = '__all__'