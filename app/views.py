from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from app.models import Profile, Post
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
            try:
                user = User.objects.get(username=username)
                messages.info(request, "Incorrect password")
            except User.DoesNotExist:
                messages.info(request, "Username does not exist")

            return redirect('signin')

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


def post_page_user(request, username):

    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
            rec_image = request.FILES['image']
            rec_name = request.POST['rec_name']
            ingredient = request.POST['ingredient']
            steps = request.POST['steps']
            avgTime = request.POST['avgTime']
            servings = request.POST['servings']
            category = request.POST['category']

            try:
                new_profile = Post(user=user, recipe_name=rec_name, ingredients=ingredient, steps_to_make=steps,
                                   average_cooking_time=avgTime, servings=servings, category=category, image=rec_image)
                new_profile.save()
            except:
                messages.info(request, "Post not Done")
                return redirect('post1')

            return redirect('explore1', username=username)  # Redirect to explore1 view with the username argument

    else:
        profile_data = user.profile

        context = {
            'user': user,
            'profile_data': profile_data,
        }

        return render(request, 'post1.html', context)


def explore_page(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'explore.html', context)


def explore_page_user(request, username):
    posts = Post.objects.all()

    context = {
        'username': username,
        'posts': posts,
    }

    return render(request, 'explore1.html', context)


def recipe_details(request, username, recipe_id):
    post = get_object_or_404(Post, id=recipe_id)

    context = {
        'username': username,
        'post': post,
    }

    return render(request, 'recipe_details.html', context)


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

def profile(request, username):
    user = request.user
    profile_data = user.profile

    context = {
        'user': user,
        'profile_data': profile_data,
    }

    return render(request, 'profile.html', context)