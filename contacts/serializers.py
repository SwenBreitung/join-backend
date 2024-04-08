from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import  IndependentContact

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndependentContact
        fields = ['name', 'color','email','phone_number']
