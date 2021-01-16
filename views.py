from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'homepage/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                new_user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
                new_user.is_active = True
                new_user.first_name = request.POST['firstname']
                new_user.last_name = request.POST['lastname']
                new_user.save()
                return redirect('loginuser')
        else:
            return render(request, 'homepage/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'homepage/signup.html')

def loginuser(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'homepage/loginuser.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'homepage/loginuser.html')

@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('signup')


def home(request):
    return render(request, 'homepage/home.html')