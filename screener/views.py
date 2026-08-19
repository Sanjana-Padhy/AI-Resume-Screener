from django.shortcuts import render, redirect
from .forms import CandidateForm
from .utils import extract_text_from_resume

def upload_resume(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            extracted = extract_text_from_resume(candidate.resume_file.path)
            candidate.extracted_text = extracted
            candidate.save()
            return redirect('upload_success')
    else:
        form = CandidateForm()

    return render(request, 'screener/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'screener/success.html')