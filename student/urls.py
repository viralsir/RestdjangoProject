from django.urls import path
from .views import *
urlpatterns = [
   path('',overview,name="home"),

   path('add',add_student,name="add"),
   path('view',view_student,name="view"),
   path('update/<int:pk>',update_student,name="update"),

   path('delete/<int:pk>',delete_student,name="delete"),

   path('',add_student,name="add"),
   path('',view_student,name="view"),
   path('',update_student,name="update"),

   path('',delete_student,name="delete"),




]


