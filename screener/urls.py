from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # Old template-based views (keep for now)
    path('upload/', views.upload_resume, name='upload_resume'),
    path('upload/success/<int:candidate_id>/', views.upload_success, name='upload_success'),
    path('candidates/', views.candidate_list, name='candidate_list'),

    # New API endpoints for React
    path('api/upload/', api_views.upload_resume_api, name='upload_resume_api'),
    path('api/candidates/', api_views.candidate_list_api, name='candidate_list_api'),
    path('api/candidates/<int:candidate_id>/', api_views.candidate_detail_api, name='candidate_detail_api'),
]