from django.shortcuts import render
from django.shortcuts import redirect
from .models import students_data
def homepage(request):
    student=students_data.objects.all()
    return render(request,'homepage.html',{'student':student})
def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
        students_data(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        course=request.POST.get('course'),
        fee=request.POST.get('fee'),
        assignment1=request.POST.get('ass1'),
        assignment2=request.POST.get('ass2'),
        assignment3=request.POST.get('ass3'),
        assignment4=request.POST.get('ass4'),
        institute=request.POST.get('institute'),
        location=request.POST.get('location'),
        ).save()
        return redirect('homepage')
def update_student(request,id):
    student=students_data.objects.get(id=id)
    if request.method=='GET':
        return render(request,'update_student.html',{'student':student})
    else:
        student.first_name=request.POST.get('fname')
        student.last_name=request.POST.get('lname')
        student.course=request.POST.get('course')
        student.fee=request.POST.get('fee')
        student.assignment1=request.POST.get('ass1')
        student.assignment2=request.POST.get('ass2')
        student.assignment3=request.POST.get('ass3')
        student.assignment4=request.POST.get('ass4')
        student.institute=request.POST.get('institute')
        student.location=request.POST.get('location')
        student.save()
        return redirect('homepage')

def delete_student(request,id):
    student=students_data.objects.get(id=id)
    student.delete()
    return redirect('homepage')

