from django.shortcuts import render,redirect
from .models import *
from .serializer import *
from .forms import *
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
#third party 
@api_view(['GET'])
def home(request):
    student=students_data.objects.all()
    serializer=students_data_serializer(student,many=True)
    return render(request, "home.html", {"students": serializer.data})



@api_view(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = create_new_student_form(request.data)
        serializer=students_data_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("home")
    else:
        form = create_new_student_form()

    return render(request, "create.html", {"form": form})
#@api_view(['PUT'])
"""
@api_view(["GET",'PUT'])
def update(request,id):
    stu=students_data.objects.get(id=id)
    if request.method=="GET":
      return render(request, "update.html", {"stu": stu})
    if request.method=="PUT":
       serializer=students_data_serializer(instance=stu,data=request.data)
       if serializer.is_valid(): 
        serializer.save()
        return redirect("home")
        
   
      
        
    return render(request, "update.html",{"stu":stu})
"""
@require_http_methods(["GET","PUT","POST"])
def update(request, id):
    try:
        stu = students_data.objects.get(id=id)
    except students_data.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
    if request.method == 'GET':
        return render(request, "update.html", {"stu": stu})
    
    if request.method in ['PUT', 'POST']:
        stu=create_new_student_form(request.POST,instance=stu)
        serial = students_data_serializer(instance=stu,data=request.data)
        if serial.is_valid():
            serial.save()
            return redirect("home")
        

    #return render(request, "update.html", {"stu": stu})

@api_view(['DELETE'])
def delete(request,id):
    stu=students_data.objects.get(id=id)
    stu.delete()
    return redirect("home")
    
