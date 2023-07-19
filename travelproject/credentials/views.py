from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):

    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return render(request, 'login.html')

    return render(request,'login.html')


def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2 = request.POST['password2']

        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')

            user=User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname,email=email)
            user.save();
            messages.info(request, "User created")
            return redirect('login')
            # print("User created")
        else:
            messages.info(request, "Password not matching")
            # print("Password not matching")

    return render(request,"register.html")