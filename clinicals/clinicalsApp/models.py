from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=20)

    last_name = models.CharField(max_length=20)

    age = models.IntegerField()

    def __str__(self):
        return self.first_name +self.last_name

class ClinicalData(models.Model):
    COMPONENT_NAMES = [('hw','Height/Weight'),('bp','Blood Pressure'),('heart rate','Heart Rate')]

    component_name = models.CharField(max_length=20, choices=COMPONENT_NAMES)

    component_Value = models.CharField(max_length=20)

    measured_DAteTime = models.DateTimeField(auto_now_add=True)

    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)   