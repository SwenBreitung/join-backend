from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
from rest_framework.decorators import action
from django.contrib.auth import authenticate

# Create your views here.


class LoginView(APIView):
    def post(self, request):
        print("Start api_login view")
        
        # Überprüfen, ob die Anforderungsdaten korrekt sind
        print("Received data:", request.data)
        
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer is valid")
            
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            
            # Überprüfen, ob der Benutzername und das Passwort korrekt sind
            print("Username:", username)
            print("Password:", password)
            
            # Benutzer anhand des Benutzernamens und des Passworts authentifizieren
            user = authenticate(username=username, password=password)
            
            if user is not None:
                print("User authenticated successfully")
                
                # Erstellen oder Abrufen des Authentifizierungstokens
                token, created = Token.objects.get_or_create(user=user)
                
                print("Token created:", token.key)
                
                # Rückgabe des Tokens
                return Response({'token': token.key})
            else:
                print("Invalid credentials")
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class LoginView(APIView):
#     @action(methods=['post'], detail=False)
#     def api_login(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get('email')
#             password = serializer.validated_data.get('password')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key})
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
# class LoginView(APIView):
#       def post(self, request):
#         print("Start api_login view")
        
#         # Überprüfen, ob die Anforderungsdaten korrekt sind
#         print("Received data:", request.data)
        
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             print("Serializer is valid")
            
#             email = serializer.validated_data.get('email')
#             password = serializer.validated_data.get('password')
            
#             # Überprüfen, ob die E-Mail und das Passwort korrekt sind
#             print("Email:", email)
#             print("Password:", password)
#             # user = authenticate(email = request.POST.get('email'), password = request.POST.get('password'))
#             user = authenticate(email=email, password=password)
#             if user is not None :
#                 print("User authenticated successfully")
                
#                 # Erstellen oder Abrufen des Authentifizierungstokens
#                 token, created = Token.objects.get_or_create(user=user)
                
#                 print("Token created:", token.key)
                
#                 # Rückgabe des Tokens
#                 return Response({'token': token.key})
#             else:
#                 print("Invalid credentials")
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             print("Serializer errors:", serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # @action(methods=['post'], detail=False)
    # def api_login(self, request):
    #     print("Start api_login view")
        
    #     # Überprüfen, ob die Anforderungsdaten korrekt sind
    #     print("Received data:", request.data)
        
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         print("Serializer is valid")
            
    #         email = serializer.validated_data.get('email')
    #         password = serializer.validated_data.get('password')
            
    #         # Überprüfen, ob die E-Mail und das Passwort korrekt sind
    #         print("Email:", email)
    #         print("Password:", password)
            
    #         user = authenticate(email=email, password=password)
    #         if user is not None:
    #             print("User authenticated successfully")
                
    #             # Erstellen oder Abrufen des Authentifizierungstokens
    #             token, created = Token.objects.get_or_create(user=user)
                
    #             print("Token created:", token.key)
                
    #             # Rückgabe des Tokens
    #             return Response({'token': token.key})
    #         else:
    #             print("Invalid credentials")
    #             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         print("Serializer errors:", serializer.errors)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=status.HTTP_200_OK)
#         return Response({"message": "Ungültige Anmeldedaten"}, status=status.HTTP_400_BAD_REQUEST)