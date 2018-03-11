from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            request.session['message'] = "Registration successful"
            return redirect('signin')
    return render(request, 'signup.html', {'form' : form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['UserName']
            password = form.cleaned_data['Password'] # give the exact name as you give in the forms.py
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'signin.html', {'form' : form, 'msg' : 'user not found'})
            else:
                login(request, user)
                return redirect('dashboard')

    if 'message' in request.session:
        msg = request.session['message']
        del request.session['message']
        return render(request, 'signin.html', {'form': form, 'msg': msg})
    else:
        return render(request, 'signin.html', {'form': form, 'msg': ''})


def logOut(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='/signin')
def dashboard(request):
    return render(request, 'dashboard.html')

