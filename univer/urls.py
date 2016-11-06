from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^students/', views.students, name='students'),
    url(r'^univers/', views.univer, name='univers'),
    url(r'^search/', views.search, name='search'),
    url(r'^(?P<s_id>[0-9]+)/$', views.student, name='student'),
    url(r'^add/', views.add, name='add'),
    url(r'^add_student/', views.add_student, name="add_student"),
]