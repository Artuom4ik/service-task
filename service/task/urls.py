from django.urls import path

from .views import TaskViewSet


app_name = 'task'

urlpatterns = [
    path('', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='tasks'),

    path('<int:pk>/', TaskViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
    }), name='task-detail'),
]
