from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student, University

def index(request):
    students_list = Student.objects.order_by('s_name')
    template = loader.get_template('univer/index.html')
    context = {
        'students_list': students_list,
    }
    return HttpResponse(template.render(context, request))

def student(request, s_id):
    stud = Student.objects.get(id=s_id)
    return HttpResponse("Page of %s." % stud)