from django.shortcuts import render
from .models import Jobs

# Create your views here

def cv_page(request):
    job = Jobs.objects.all().order_by("job_title")
    return render(request, "cv_page.html", {"jobs": job})

def job_desc_page(request, slug):
    job = Jobs.objects.get(slug=slug)
    return render(request, "job_desc_page.html", {"job": job})