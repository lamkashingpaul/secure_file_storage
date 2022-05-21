from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('files/', views.all_files, name='list_files'),
    path('upload/', views.upload_file, name='upload_file'),
    path('remove/<int:file_id>/', views.remove_file, name='remove_file'),
]
