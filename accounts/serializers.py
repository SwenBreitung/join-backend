from django import forms
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  
    password = serializers.CharField()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        email = forms.EmailField(required=True)
        model = User     
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Die beiden Passwörter stimmen nicht überein.'})
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    

# class RegisterView(APIView):
#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         if email and password:
#             password = make_password(password)
#             user = User.objects.create(email=email, password=password)
#             return Response({'success': True, 'message': 'User successfully registered'})
#         else:
#             return Response({'success': False, 'message': 'Email and password are required'})

# # Und fügen Sie die entsprechende URL zu Ihrer urls.py hinzu
# from django.urls import path
# from .views import RegisterView
