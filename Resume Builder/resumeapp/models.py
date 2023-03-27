from django.db import models

# Create your models here.
class Resumedata(models.Model):
    name=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    address=models.TextField(max_length=1000,null=True)
    objective=models.TextField(max_length=1000,null=True)
    institution=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=100,null=True)
    percentage=models.CharField(max_length=100,null=True)
    skill=models.TextField(max_length=100,null=True)
    project=models.TextField(max_length=1000,null=True)
    experience=models.TextField(max_length=1000,null=True)
    declaration=models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.name