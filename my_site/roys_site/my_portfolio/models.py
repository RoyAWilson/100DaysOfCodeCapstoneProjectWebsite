from django.db import models

# Create your models here.
class Portfolio(models.Model):
    project_title = models.CharField(max_length=150)
    project_img = models.ImageField(blank=True)
    Project_desc = models.TextField()
    date_completed = models.DateField()
    project_url = models.URLField(max_length=200, default="Enter URL here")
    project_slug = models.SlugField(default="abcdef")

    def __str__(self):
        return self.project_title
    