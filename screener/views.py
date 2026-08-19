from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidateForm
from .utils import extract_text_from_resume
from .ai_scorer import score_resume
from .models import Candidate

def upload_resume(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()

            extracted = extract_text_from_resume(candidate.resume_file.path)
            candidate.extracted_text = extracted

            score, feedback = score_resume(extracted, candidate.job_description)
            candidate.ai_score = score
            candidate.ai_feedback = feedback
            candidate.status = 'scored'

            candidate.save()
            return redirect('upload_success', candidate_id=candidate.id)
    else:
        form = CandidateForm()

    return render(request, 'screener/upload.html', {'form': form})


def upload_success(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    return render(request, 'screener/success.html', {'candidate': candidate})


def candidate_list(request):
    candidates = Candidate.objects.filter(status='scored').order_by('-ai_score')
    return render(request, 'screener/candidate_list.html', {'candidates': candidates})