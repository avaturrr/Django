from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, related_name="students")

    def __str__(self):
        return f"{self.name} - {self.lastname}"


class Diary(models.Model):
    grade_point_average = models.FloatField()
    student = models.OneToOneField("Student", null=True, on_delete=models.SET_NULL, related_name="diary")

