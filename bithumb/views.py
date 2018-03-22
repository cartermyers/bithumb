from django.shortcuts import render

from account.forms import SignupForm, LoginForm

def index(request):
    total_in_game_currency = None
    if request.user.is_authenticated:
        total_in_game_currency = request.user.get_bank_account().get_in_game_currency()

    return render(request, 'bithumb/index.html', {'signup_form': SignupForm(), 'login_form': LoginForm(), 'total_score': total_in_game_currency})

def about(request):
    return render(request, 'bithumb/about_us.html')
