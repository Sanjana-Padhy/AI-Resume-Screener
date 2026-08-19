from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'email', 'phone', 'resume_file', 'job_description',
                  'ai_score', 'ai_feedback', 'status', 'uploaded_at']
        read_only_fields = ['ai_score', 'ai_feedback', 'status', 'uploaded_at']