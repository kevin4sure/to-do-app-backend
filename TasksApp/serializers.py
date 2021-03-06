from rest_framework import serializers

from .models import Task, Bucket

class TaskSerializer(serializers.ModelSerializer):
    bucket_id = serializers.CharField(write_only=True,required=True)
    bucket = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'
        
    
    def get_bucket(self, instance):
        try:
            return BucketSerializer(Bucket.objects.get(id=instance.bucket.id)).data
        except AttributeError:
            return None 

    def create(self, validated_data):
        new_task = Task.objects.create(**validated_data)
        return new_task

    def update(self,obj ,validated_data, *args, **kwargs):
        # try: validated_data.pop('validated_data')
        # except IndexError: pass
        # except KeyError: pass
        return super().update(obj,validated_data,*args, **kwargs) 


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'

    def create(self, validated_data):
        new_bucket = Bucket.objects.create(**validated_data)
        return new_bucket

