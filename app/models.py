from django.db import models

# Create your models here.
from django.urls import reverse



class Employee(models.Model):
    EmployeeId = models.IntegerField(primary_key = True)
    EmployeeName = models.CharField(max_length = 30)
    Department = models.CharField(max_length = 30)
    Plant = models.CharField(max_length = 30)
    Designation = models.CharField(max_length = 30)
    Location = models.CharField(max_length = 30)

    def __str__(self):
        return self.EmployeeName


    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})