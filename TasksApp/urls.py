from django.urls import path

from .views import TasksView

urlpatterns = [
    path('',TasksView.as_view({'get':'list','post':'create'})),
    path('task/<int:pk>', TasksView.as_view({'put':'partial_update','delete':'delete'}))
]
