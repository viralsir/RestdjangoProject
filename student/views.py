from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student

from student.Serializers import StudentSerializer


# Create your views here.
@api_view(['GET'])
def overview(request):
    student={
        "name":"vimal",
        "course":"java"
    }
    return Response(student)

@api_view(['POST'])
def add_student(request):
    student=StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
        return Response(student.data, status=status.HTTP_201_CREATED)
    else :
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_student(request):
    students=student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_student(request,pk):
    Student=student.objects.get(pk=pk)
    serializer=StudentSerializer(Student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request,pk):
    Student=student.objects.get(pk=pk)
    Student.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


