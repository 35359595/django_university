from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<s_id>[0-9]+)/$', views.student, name='student'),
]