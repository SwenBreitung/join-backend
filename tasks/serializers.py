from django.contrib.auth.models import Group, User
from rest_framework import serializers
from tasks.models import Task, Subtask, Contact
from django.db import transaction

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'name', 'status']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'color']

class TasksSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'user', 'subtasks', 'contacts', 'status','category','priority','date']
        read_only_fields = ['id', 'created_at', 'user']

    def create(self,  validated_data):
        # Extrahiere 'subtasks' und 'contacts' Daten aus validated_data
        subtasks_data = validated_data.pop('subtasks', [])
        contacts_data = validated_data.pop('contacts', [])

        # Erstelle das Task-Objekt
        task = Task.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        for contact_data in contacts_data:
            Contact.objects.create(task=task, **contact_data)

        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        contacts_data = validated_data.pop('contacts', [])
  
        # Aktualisiere das Task-Objekt
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Lösche alle vorhandenen Contacts und füge die neuen hinzu
        instance.contacts.all().delete()
        for contact_data in contacts_data:
            Contact.objects.create(task=instance, **contact_data)

        # Update Subtasks (optional)
        instance.subtasks.all().delete()
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=instance, **subtask_data)

        return instance



