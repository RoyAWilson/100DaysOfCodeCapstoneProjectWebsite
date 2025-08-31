from django.shortcuts import render
from .models import Jobs

# Create your views here

def cv_page(request):
    job = Jobs.objects.all().order_by("job_title")
    return render(request, "cv_page.html", {"jobs": job})