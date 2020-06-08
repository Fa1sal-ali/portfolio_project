from django.db import models

class Input(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
