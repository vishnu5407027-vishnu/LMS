from django.shortcuts import render

def login_view(request):
    return render(request, 'index.html')

def register_view(request):
    return render(request, 'register.html')

def courses_view(request):
    return render(request, 'courses.html')

def assignments_view(request):
    return render(request, 'assignments.html')
