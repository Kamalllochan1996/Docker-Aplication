from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
# myapp/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# from myapp.serializers import BookSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.serializers import UserSerializer
import datetime

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class ObtainTokenPairView(TokenObtainPairView):
#     pass

class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Get the user information from the request body
        user_data = request.data.get('user')

        # Check if the user information is provided
        if not user_data:
            return Response({'error': 'User information not provided'})

        # Get the user
        try:
            user = User.objects.get(username=user_data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'})

        # Serialize the user data
        serializer = UserSerializer(user)

        # Check if the user is a new user
        date_joined = datetime.datetime.strptime(serializer.data['date_joined'], '%Y-%m-%dT%H:%M:%S.%fZ')
        is_new_user = (datetime.datetime.now() - date_joined).days <= 7

        # Return the user data with the `is_new_user` field
        data = serializer.data
        data['is_new_user'] = is_new_user
        return Response(data)