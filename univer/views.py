from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student, University

def index(request):
    template = loader.get_template('univer/index.html')
    return HttpResponse(template.render(request))

def students(request):
    students_list = Student.objects.order_by('s_name')
    template = loader.get_template('univer/index.html')
    context = {
        'students_list': students_list,
    }
    return HttpResponse(template.render(context, request))

def student(request, s_id):
    stud = Student.objects.get(id=s_id)
    template = loader.get_template('univer/index.html')
    context = {
        'stud_personal': stud,
    }
    return HttpResponse(template.render(context, request))

def univer(request):
    univers = University.objects.order_by('u_name')
    template = loader.get_template('univer/index.html')
    context = {
        'univers_list': univers,
    }
    return HttpResponse(template.render(context, request))