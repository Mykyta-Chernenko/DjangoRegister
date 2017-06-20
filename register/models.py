from django.db import models
from enum import Enum


class Subject(models.Model):
    subject = models.TextField(max_length=20)
    def __str__(self):
        return self.subject.__str__()


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    classroom = models.CharField(max_length=6)
    def __str__(self):
        return self.name + " " + self.surname


class Grade(models.Model):
    grade_number = models.CharField(max_length=4)
    head_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    def __str__(self):
        return " Class № " + self.grade_number + " Head: " + " " + self.head_teacher.__str__()

class GradeSubject(models.Model):
    grade = models.ForeignKey(Grade)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    def __str__(self):
        return self.grade.__str__() + ' ' + self.subject.__str__() + " " + self.teacher.__str__()

class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    class_name = models.ForeignKey(Grade,on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " +self.surname + " " +self.class_name.__str__()


class Mark(models.Model):
    datetime = models.DateTimeField( auto_now_add=True)
    value = models.SmallIntegerField()
    subject = models.ForeignKey(Subject)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.student.__str__() + " Value "  +self.value.__str__() + " Subject " +self.subject.__str__()+ " Date " + self.datetime.strptime("%d/%m/%Y %H:%M").__str__()