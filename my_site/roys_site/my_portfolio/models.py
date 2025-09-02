from django.db import models

# Create your models here.
class Portfolio(models.Model):
    project_title = models.CharField(max_length=150)
    project_img = models.ImageField(blank=True)
    Project_desc = models.TextField()
    date_completed = models.DateField()

    def __str__(self):
        return self.project_title
    