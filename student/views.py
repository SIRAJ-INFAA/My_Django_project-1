from django.shortcuts import render, get_object_or_404
from .models import Student, SubjectMarks
from django.http import HttpResponse, Http404

def student_detail(request):
    stud = Student.objects.all()
    
    return render(request, 'student/student_detail.html',{'all_stud': stud})

def student_induv(request, id):
   student = Student.objects.get(pk=id)
   subject_marks = SubjectMarks.objects.get(pk=id)

   return render(request, 'student/student_indu.html', {'stud': student, 'sub_marks': subject_marks})
    
    
    

