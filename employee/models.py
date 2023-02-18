from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    dob = models.DateField()
    dept_name = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name
