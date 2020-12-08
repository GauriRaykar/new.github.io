from django.db import models

class Submission(models.Model):
    
    question= models.CharField(max_length=500)


  