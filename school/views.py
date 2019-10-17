from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.order_by(ordering).prefetch_related('teacher')
    object_list = []
    for s in students:
        teachers = []
        for t in s.teacher.all():
            teachers.append({'name': t.name, 'subject': t.subject})
        object_list.append({'name': s.name, 'group': s.group, 'teachers': teachers})
    context = {
        'object_list': object_list
    }
    return render(request, template, context)
