from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    tags = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
     