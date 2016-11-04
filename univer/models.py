from django.db import models

class University(models.Model):
    u_name = models.CharField(max_length=200)
    u_city = models.CharField(max_length=200)
    u_uri = models.URLField(max_length=200)

    def __str__(self):
        return self.u_name + " of " + self.u_city

class Cathedra(models.Model):
    c_name = models.CharField(max_length=200)
    c_univer = models.ForeignKey(University, null=True)

    def __str__(self):
        return self.c_name

class Disciplin(models.Model):
    d_name = models.CharField(max_length=200)
    d_cathedra = models.ForeignKey(Cathedra)

    def __str__(self):
        return self.d_name + " is lectured on " + self.d_cathedra

class HomeTask(models.Model):
    ht_name = models.CharField(max_length=200)
    ht_disciplin = models.ForeignKey(Disciplin)
    accomplished = models.BooleanField(default=False)

    def __str__(self):
        return self.ht_name

class Student(models.Model):
    s_name = models.CharField(max_length=20)
    s_las_name = models.CharField(max_length=35)
    s_email = models.EmailField(max_length=254)
    s_phone = models.PositiveIntegerField()
    s_university = models.ForeignKey(University)
    s_cathedra = models.ForeignKey(Cathedra)
    s_disciplins = models.ForeignKey(Disciplin)
    s_ht = models.ForeignKey(HomeTask)

    def __str__(self):
        return self.s_name + " studiing " + self.s_cathedra + " in " + self.s_university

class Lector(models.Model):
    l_name = models.CharField(max_length=20)
    l_las_name = models.CharField(max_length=35)
    l_students = models.ForeignKey(Student)
    l_univer = models.ForeignKey(University, null=True)
    l_cathedra = models.ForeignKey(Cathedra, null=True)

    def __str__(self):
        return self.l_name + " teaching at " + self.l_univer