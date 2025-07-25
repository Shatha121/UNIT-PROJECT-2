from django.db import models


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
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='incidents/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    reporter_name = models.CharField(max_length=100, default="Anonymous", blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)

    def reporter_rank(self):
        if self.reporter_name.lower().strip() == "anonymous":
            return None
        count = Incident.objects.filter(reporter_name = self.reporter_name).count()
        if count >= 10:
            return 'Gold'
        elif count >= 5:
            return "Silver"
        return 'Bronze'

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.incident.title}"

