from django.db import models
from django.core.validators import MaxValueValidator,MaxLengthValidator,MinLengthValidator

# Create your models here.


class Patient(models.Model):
    Choices = [("Male","male"),("Female","Female"),("Others","Others")]
    patient_id = models.BigAutoField(primary_key=True)
    patient_name = models.CharField(max_length=40)
    patient_age = models.IntegerField(validators=[MaxValueValidator(100,message="Enter age less than 100")])
    gender = models.CharField(choices=Choices,default="Male",max_length=10)
    patient_report_id = models.CharField(default=models.SET_NULL,max_length=24,validators=[MaxLengthValidator(24),MinLengthValidator(24)])