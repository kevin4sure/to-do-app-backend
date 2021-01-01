from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        new_task = Task.objects.create(**validated_data)
        return new_task

    def update(self,obj ,validated_data, *args, **kwargs):
        # try: validated_data.pop('validated_data')
        # except IndexError: pass
        # except KeyError: pass
        return super().update(obj,validated_data,*args, **kwargs)        
