from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<resId>/', views.task_result, name='task_result'),
    
]