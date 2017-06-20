from django.contrib import admin
from .models import Student,Grade,Teacher,Mark,GradeSubject,Subject

admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(GradeSubject)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Mark)

