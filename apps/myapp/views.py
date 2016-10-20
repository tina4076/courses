from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context= {
    'courses' : Course.objects.all()
    }
    return render(request,'myapp/index.html', context)

def add(request):
    name = request.POST['course_name']
    description = request.POST['course_description']
    Course.objects.create(name = name, description =description)
    return redirect('/')

def destroy(request, id):
    course = Course.objects.filter(id = id)
    context = {
    'id' : id,
    'name': course[0].name,
    'description': course[0].description
    }
    return render(request, 'myapp/destroy.html', context)

def confirm(request,id):
    #print "Request = ", request.POST
    if "Yes" in request.POST:
        Course.objects.filter(id = id).delete()
    return redirect('/')
