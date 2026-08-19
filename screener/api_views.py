from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as http_status

from .models import Candidate
from .serializers import CandidateSerializer
from .utils import extract_text_from_resume
from .ai_scorer import score_resume


@api_view(['POST'])
def upload_resume_api(request):
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        candidate = serializer.save()

        extracted = extract_text_from_resume(candidate.resume_file.path)
        candidate.extracted_text = extracted

        score, feedback = score_resume(extracted, candidate.job_description)
        candidate.ai_score = score
        candidate.ai_feedback = feedback
        candidate.status = 'scored'
        candidate.save()

        result_serializer = CandidateSerializer(candidate)
        return Response(result_serializer.data, status=http_status.HTTP_201_CREATED)

    return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def candidate_list_api(request):
    candidates = Candidate.objects.filter(status='scored').order_by('-ai_score')
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def candidate_detail_api(request, candidate_id):
    try:
        candidate = Candidate.objects.get(id=candidate_id)
    except Candidate.DoesNotExist:
        return Response({'error': 'Candidate not found'}, status=http_status.HTTP_404_NOT_FOUND)

    serializer = CandidateSerializer(candidate)
    return Response(serializer.data)