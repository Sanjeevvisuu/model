from django.db import models

# Create your models here.
class students_data(models.Model):
    name=models.CharField(max_length=50)
    std=models.CharField(max_length=2)
    section=models.CharField(max_length=1)
    school=models.CharField(max_length=200)
    ph_no = models.CharField(max_length=20,unique=True) 

    def __str__(self):
        return self.name