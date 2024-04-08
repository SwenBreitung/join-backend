from django.shortcuts import render
from .models import IndependentContact
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import  ContactSerializer

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = IndependentContact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        contact_data = request.data.copy()
        contact = self.create_task(contact_data)  
        contact_serializer = self.get_serializer(contact)
        return Response(contact_serializer.data, status = status.HTTP_201_CREATED)


# Create your views here.
