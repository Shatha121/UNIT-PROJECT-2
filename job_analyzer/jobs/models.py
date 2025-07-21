from django.db import models


# Create your models here.
class Job(models.Model):

    CATEGORY_CHOICES = [
        ("frontend","Frontend"),
        ("backend","Backend"),
        ("fullstack","Full Stack"),
        ("data", "Data Science"),
        ("devops", "DevOps"),
        ("other", "Others")
    ]

    title = models.CharField(max_length=200)
    description = models.TextField() #Full details of the job cames from the User
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    overall_rating = models.CharField(max_length=10, choices=[
        ('green','Green'),
        ('yellow',"Yellow"),
        ('red',"Red"),
    ], blank=True, null=True) # comes from the ai

    overall_score = models.FloatField(blank=True, null=True) # from 0 - 100 based on the clarity , compliance or legality. comes from the ai

    def __str__(self):
        return self.title
    
class JobAnalysis(models.Model): #this would give you the line by line analysis
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    #remember to change it later
    line_number = models.IntegerField(blank=True, null=True) #the line number in the original job description. Helps you keep track of which comment refers to which line
    line_text = models.TextField(blank=True, null=True) # the actual line of text the AI is ananlyzing (pulled from the full description)
    ai_comment = models.TextField() # Ai feedback for this specific line
    rating = models.CharField(max_length=10, choices=[
        ('green','Green'),
        ('yellow',"Yellow"),
        ('red',"Red"),
    ],blank=True, null=True)

    def __str__(self):
        return f"Line {self.line_number} of {self.job.title}"