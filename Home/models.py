from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class About(models.Model):
    Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Description = models.TextField(max_length=500, default="")
    Image = models.ImageField(upload_to="Home/images", default="")
    Facebook = models.URLField(blank=True)
    Insta = models.URLField(blank=True)
    Twitter = models.URLField(blank=True)

    def __str__(self):
        return self.Name


class ContactUs(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

