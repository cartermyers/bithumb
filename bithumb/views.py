from django.shortcuts import render

from account.forms import SignupForm, LoginForm

def index(request):
    return render(request, 'bithumb/index.html', {'signup_form': SignupForm(), 'login_form': LoginForm()})

def about(request):
    return render(request, 'bithumb/about_us.html')
