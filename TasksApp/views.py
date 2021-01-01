from rest_framework import views
from rest_framework.response import Response 

from .models import Task
from .serializers import TaskSerializer

class TasksView(views.APIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self, **kwargs):
        return self.queryset.filter(**kwargs)
    

    def get(self, request):
        all_tasks = self.get_queryset()
        serializer = self.serializer_class(all_tasks, many=True).data
        return Response(serializer)
                        