from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeprofile', user=user.username)  # Redirect to user's profile
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if len(password) < 8:
                messages.info(request, "Password must be at least 8 characters long")
                return redirect('signup')
            else:
                try:
                    User.objects.get(email=email)
                    messages.info(request, "Email already exists")
                    return redirect('signup')
                except User.DoesNotExist:
                    pass

                try:
                    User.objects.get(username=username)
                    messages.info(request, "Username already exists")
                    return redirect('signup')
                except User.DoesNotExist:
                    pass

                user = User(first_name=firstname, last_name=lastname, email=email, username=username)
                user.set_password(password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile(username=user_model, id_user=user_model, firstname=firstname, lastname=lastname,
                                      email=email, password=password)
                new_profile.save()
            return redirect('home')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def post(request):
    return render(request, 'post.html')


def explore(request):
    return render(request, 'explore.html')


def homeprofile(request, username):
    user = User.objects.get(username=username)
    profile_data = user.profile

    context = {
        'user': user,
        'profile_data': profile_data,
    }

    return render(request, 'homeprofile.html', context)
