from django.shortcuts import render

# Create your views here.
# myapp/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView




class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class ObtainTokenPairView(TokenObtainPairView):
#     pass
