

from django.contrib import admin
from django.urls import path
from task import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create_todo, name='create'),
    path('edit/<int:pk>/', views.edit_todo, name='edit'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('completed/', views.completed, name='completed'),
]
