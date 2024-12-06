from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create_project/', views.createProjects, name='createprojects'),
    path('update_project/<str:pk>/', views.updateProject, name='updateproject'),
    path('delete_project/<str:pk>/', views.deleteProject, name='deleteproject'),
]

