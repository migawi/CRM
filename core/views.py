from django.shortcuts import render

# Create your views here.

def homeview(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
