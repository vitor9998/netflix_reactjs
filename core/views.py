from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login


# Create your views here.

def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login/#')
        else:
            message.error(request, 'Usuário e senha inválido. Favor tentar novamente.')
    return redirect('/login')

