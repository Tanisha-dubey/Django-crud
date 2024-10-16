from django.db import models


class Student(models.Model):
    stu_name=models.CharField(max_length=150)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_password=models.CharField(max_length=25)

def __str__(self):
    return self.stu_name


class Query(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_query=models.TextField(max_length=50)

def _str_(self):
    return self.stu_query

