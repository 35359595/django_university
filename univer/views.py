from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Student, University, Cathedra, HomeTask, Disciplin

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

def search(request):
    search_request = request.GET['search_box']
    result = Student.objects.filter(
        Q(s_name__icontains=search_request) | Q(s_las_name__icontains=search_request))
    # template = loader.get_template('univer/index.html')
    context = { 'search_form': result, }
    return render(request, 'univer/index.html', context)
    #return HttpResponse(template.render(context, request))

def add(request):
    return render(request, 'univer/add.html')

def add_student(request):
    name = request.GET['add_name']
    last_name = request.GET['add_last_name']
    phone = request.GET['add_phone']
    mail = request.GET['add_mail']
    cath = Cathedra.objects.get(id=2)
    uni = University.objects.get(id=1)
    ht = HomeTask.objects.get(id=1)
    dc = Disciplin.objects.get(id=2)
    stud = Student(s_name=name, s_las_name=last_name, s_email=mail, s_phone=phone, 
            s_cathedra=cath, s_university=uni, s_disciplins=dc, s_ht=ht)
    stud.save()
    students_list = Student.objects.order_by('s_name')
    context = { 'students_list': students_list, }
    return render(request, 'univer/index.html', context)