from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Incident(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    CATEGORY_CHOICES = [
        ('public_safety', 'Public Safety'),
        ('road_damage', 'Road Damage'),
        ('vandalism', 'Vandalism'),
        ('sanitation', 'Sanitation'),
        ('lighting', 'Lighting'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='incidents/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title