from django.http import HttpResponse
from django.shortcuts import render

from .models import Subject, Grade,GradeSubject
from django.template import RequestContext, loader


def index(request):
    all_grades = Grade.objects.all()
    grades_with_subjects = {}
    for grade in all_grades:
        grades_with_subjects[grade] = GradeSubject.objects.filter(grade__grade_number=grade.grade_number)
    context = {'grades_with_subjects': grades_with_subjects}
    i = 0
    for x in grades_with_subjects.keys():
        for g in grades_with_subjects.get(x):
            i+=1
    return render(request, 'register/index.html', context)