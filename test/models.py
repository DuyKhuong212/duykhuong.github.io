import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import SET_NULL


class User(AbstractUser):
    clas = models.CharField(max_length=12, null=True)
    adress = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.username
class Award(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name =models.CharField(max_length=100)
    price =models.FloatField()
    desc =models.CharField(max_length=100)
    def __str__(self):
        return self.name
class FormApply(models.Model):
    student_id=models.ForeignKey(User,on_delete=SET_NULL,null=True)
    award_id = models.ForeignKey(Award,on_delete=SET_NULL,null=True)
    context = models.FileField()
    status =models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.status
class StudentTranscript(models.Model):
    poin =models.FloatField()
    name =models.CharField(max_length=50,null=True)
    student_id=models.ForeignKey(User,on_delete=SET_NULL,null=True)
    def __str__(self):
        return self.poin
