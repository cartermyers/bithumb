from django.shortcuts import render

def index(request):
    return render(request, 'bithumb/index.html')

def about(request):
    return render(request, 'bithumb/about_us.html')
