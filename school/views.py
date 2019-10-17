from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.order_by(ordering).prefetch_related('teacher').values('name', 'group', 'teacher__name', 'teacher__subject')
    object_list = []
    students_counter = []
    for s in students:
        if s['name'] not in students_counter:
            students_counter.append(s['name'])
            object_list.append({'name': s['name'], 'group': s['group'], 'teachers': [{'name': s['teacher__name'], 'subject': s['teacher__subject']}]})
        else:
            for o in object_list:
                if o['name'] == s['name']:
                    o['teachers'].append({'name': s['teacher__name'], 'subject': s['teacher__subject']})
    context = {
        'object_list': object_list
    }
    return render(request, template, context)
