from django.shortcuts import get_object_or_404
from rest_framework import views, status, permissions
from rest_framework.response import Response 

from .models import Task
from .serializers import TaskSerializer

class TasksView(views.APIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, **kwargs):
        return self.queryset.filter(**kwargs)
    

    def get(self, request):
        all_tasks = self.get_queryset()
        serializer = self.serializer_class(all_tasks, many=True).data
        return Response(serializer)
                        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'msg': 'task added successfully'}, status=status.HTTP_201_CREATED)
        else: return Response({'error':serializer.errors,'msg':'can\'t create new task.'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class UpdateTaskView(views.APIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk=None):
        serializer = self.serializer_class(data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            task_obj = get_object_or_404(Task, id=pk) 
            task = serializer.update(task_obj,serializer.validated_data)
            serialized = self.serializer_class(instance=task).data
            return Response({'msg': 'task updated successfully', 'task': serialized})






