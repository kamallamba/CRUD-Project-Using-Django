from django.db import models

# Create your models here.
class StudentsInfo(models.Model):
    Name=models.CharField(max_length=70)
    Roll_NO=models.IntegerField(primary_key=True)
    Email=models.EmailField(max_length=100)
    
