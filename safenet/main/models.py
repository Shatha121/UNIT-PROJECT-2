from django.db import models
from incidents.models import Incident

# Create your models here.

  
class Contact(models.Model):
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.first_name + " " + self.last_name