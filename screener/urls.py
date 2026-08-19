from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    path('upload/success/<int:candidate_id>/', views.upload_success, name='upload_success'),
    path('candidates/', views.candidate_list, name='candidate_list'),
]