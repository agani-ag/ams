from django.db import models

# Create your models here.

class City(models.Model):
    city_n = models.CharField(max_length=30)

    def __str__(self):
        return self.city_n

class Course(models.Model):
    course_n = models.CharField(max_length=30)

    def __str__(self):
        return self.course_n

class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=30)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.fname +' '+self.lname