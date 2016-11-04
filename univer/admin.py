from django.contrib import admin

from .models import University, Cathedra, Student, Lector, HomeTask, Disciplin

admin.site.register(University)
admin.site.register(Cathedra)
admin.site.register(Student)
admin.site.register(Lector)
admin.site.register(HomeTask)
admin.site.register(Disciplin)