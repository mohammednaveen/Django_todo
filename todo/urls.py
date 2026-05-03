from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask, name='addTask'),
    path('deleteTask/<int:pk>/',views.deleteTask, name='deleteTask'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    path('markAsDone/<int:pk>/',views.markAsDone, name='markAsDone'),
    path('markAsUndone/<int:pk>/', views.markAsUndone, name='markAsUndone'),
]
