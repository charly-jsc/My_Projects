from django.db import models
from datetime import datetime

# Create your models here.
class Snippet(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    client_ip = models.CharField(max_length = 200, default=0)

    def __str__(self):
        return self.content
