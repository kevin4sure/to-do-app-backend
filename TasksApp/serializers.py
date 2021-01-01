from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        new_task = Task.objects.create(**validated_data)
        return new_task    
