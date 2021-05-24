from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date')
    content = models.TextField()
    writer = models.CharField(max_length=100)

    def __str__(self):
        return self.title