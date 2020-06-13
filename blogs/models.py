from django.db import models

class post(models.Model):
    title = models.CharField(max_length=50)
    date_time_stamp = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    content = models.TextField()

    def __str__(self):
        return self.title