from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import ProfileSerializer
from .models import Profile
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

#customuser
User = get_user_model()

class SignupView(APIView):
    """user creation"""
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        data = self.request.data
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'email':'Email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error':'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(name=name,email=email,password=password)
                    user.save()
                    return Response({'success':'User created successfully'})
        else:
            return Response({'error':'Passwords do not match'})

#profile_upload
from rest_framework.parsers import FileUploadParser
class ProfileView(APIView):
    parser_class = (FileUploadParser, )
    permission_classes = (permissions.IsAuthenticated, )
    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)