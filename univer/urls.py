from .api import LectorViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lector', LectorViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = router.urls 

# urlpatterns = [
#     url(r'lector'),
#     url(r'student'),
    # url(r'^students/', views.students, name='students'),
    # url(r'^univers/', views.univer, name='univers'),
    # url(r'^search/', views.search, name='search'),
    # url(r'^(?P<s_id>[0-9]+)/$', views.student, name='student'),
    # url(r'^add/', views.add, name='add'),
    # url(r'^add_student/', views.add_student, name="add_student"),
#]