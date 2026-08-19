from django.shortcuts import render, redirect
from .forms import CandidateForm

def upload_resume(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = CandidateForm()

    return render(request, 'screener/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'screener/success.html')