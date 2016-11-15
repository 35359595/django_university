from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import LectorSerializer, StudentSerializer
from .models import Lector, Student

class LectorViewSet(ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    permission_classes = (permissions.IsAuthenticated,)

class StudentViewSet(ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)