from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
