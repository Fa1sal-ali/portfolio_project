from django.db import models

class Input(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    github_link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
