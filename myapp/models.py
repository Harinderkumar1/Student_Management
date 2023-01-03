from django.db import models

# Create your models here.

Gender=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','other'),
)

class Position(models.Model):
    pname=models.CharField(max_length=255)

    def __str__(self):
        return self.pname

class student(models.Model):
    name=models.CharField(max_length=255)
    standard=models.CharField(max_length=255)
    gender=models.CharField(max_length=10,choices=Gender,default='Male',null=True,blank=True)
    # Position=models.ForeignKey(Position,on_delete=models.CASCADE)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField()


    def __str__(self):
        return self.name