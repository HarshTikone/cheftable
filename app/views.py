from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from app.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.


def index_page(request):
    return render(request, 'index.html')



def signin_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('homeprofile', user.username)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')




def signup_page(request):
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

                new_profile = Profile(user=user)
                new_profile.save()
            return redirect('signin')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def post_page(request):
    return render(request, 'post.html')


def explore_page(request):
    return render(request, 'explore.html')


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def homeprofile_page(request, username):
    user = get_object_or_404(User, username=username)
    # Retrieve additional profile data or perform any necessary operations
    profile_data = user.profile

    context = {
        'user': user,
        'profile_data': profile_data,
    }

    return render(request, 'homeprofile.html', context)


def logout_page(request, username):
    logout(request)

    return redirect('index')
