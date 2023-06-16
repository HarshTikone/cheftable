from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from app.models import Profile
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    if request.method == ['POST']:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('signup')
            elif len(password) < 8:
                messages.info(request, "Password must be 8 character long")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()

                serializer = ProfileSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return redirect('signin')

        else:
            messages.info(request, "Password not matching")
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def post(request):
    return render(request, 'post.html')


def explore(request):
    return render(request, 'explore.html')