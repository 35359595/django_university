from rest_framework import serializers
from .models import Lector, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LectorSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)
    class Meta:
        model = Lector
        fields = '__all__'