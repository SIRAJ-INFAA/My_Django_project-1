from django.urls import path
from . import views


urlpatterns = [
    path('',views.student_detail, name="student_detail"),
    path('student/<int:id>', views.student_induv, name="student_personal"),
      
]