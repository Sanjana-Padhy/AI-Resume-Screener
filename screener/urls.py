from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    path('upload/success/', views.upload_success, name='upload_success'),
]