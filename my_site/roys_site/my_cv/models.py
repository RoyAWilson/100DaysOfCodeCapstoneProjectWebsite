from django.db import models

# Create your models here.

class Jobs(models.Model):
    job_title = models.CharField(max_length=50)
    employer = models.CharField(max_length=150)
    duties = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.job_title
    
