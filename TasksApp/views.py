from django.shortcuts import get_object_or_404
from rest_framework import views, status, permissions, viewsets
from rest_framework.response import Response 
from .models import Task, Bucket
from .serializers import TaskSerializer, BucketSerializer

class TasksView(viewsets.ViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, **kwargs):
        return self.queryset.filter(**kwargs)
    

    def list(self, request):
        all_tasks = self.get_queryset()
        serializer = self.serializer_class(all_tasks, many=True).data
        return Response(serializer)
                        
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'msg': 'task added successfully'}, status=status.HTTP_201_CREATED)
        else: return Response({'error':serializer.errors,'msg':'can\'t create new task.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def partial_update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            task_obj = get_object_or_404(Task, id=pk) 
            task = serializer.update(task_obj,serializer.validated_data)
            serialized = self.serializer_class(instance=task).data
            return Response({'msg': 'task updated successfully', 'task': serialized})

    def delete(self, request, pk=None):
        task_obj = get_object_or_404(Task, id=pk)
        try:
            task_obj.delete()
            return Response({'msg': 'the task deleted successfully'})
        except Exception as e:
            return Response({'msg': 'some error occurred while attempting to delete the task', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BucketView(viewsets.ViewSet):
    serializer_class = BucketSerializer
    queryset = Bucket.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, **kwargs):
        return self.queryset.filter(**kwargs)

    def list(self, request):
        all_buckets = self.get_queryset()
        serializer = self.serializer_class(all_buckets, many=True).data
        return Response(serializer)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'msg': 'bucket added successfully'}, status=status.HTTP_201_CREATED)
        else: return Response({'error':serializer.errors,'msg':'can\'t create new bucket.'}, status=status.HTTP_406_NOT_ACCEPTABLE)








