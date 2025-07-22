from django.db import models
from incidents.models import Incident

# Create your models here.

class Comment(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.incident.title}"