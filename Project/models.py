from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    s_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Description = models.TextField(max_length=5000, default="")
    Image = models.ImageField(upload_to="Project/images", default="")
    Date = models.DateField()

    def __str__(self):
        return self.Title
