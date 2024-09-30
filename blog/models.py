from django.db import models
from django.urls import reverse


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('blog', args=[self.pk])

    def get_absolute_url2(self):
        return reverse('index')
