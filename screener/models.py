from django.db import models

class Candidate(models.Model):
    # Basic info collected at upload time
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    # The actual uploaded file + the job it's being screened against
    resume_file = models.FileField(upload_to='resumes/')
    job_description = models.TextField()

    # Filled in later by our parsing/AI logic — not required at upload time
    extracted_text = models.TextField(blank=True, null=True)
    ai_score = models.FloatField(blank=True, null=True)
    ai_feedback = models.TextField(blank=True, null=True)

    # Housekeeping
    uploaded_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('scored', 'Scored'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.name} - {self.status}"