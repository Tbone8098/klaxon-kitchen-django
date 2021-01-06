from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User

# Create your views here.


def login_redirect(request):
    return redirect('/login')


def login(request):
    return render(request, 'login/login.html')

# process


def logout(request):
    request.session.flush()
    return redirect('/')


def process_login(request):
    user = User.objects.filter(email=request.POST['email'])

    errors = User.objects.login_validation(request.POST, user)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['active_user_id'] = user[0].id
        return redirect('klaxonKitchen:home')


def process_regi(request):
    errors = User.objects.regi_user_validation(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        pw_hash = User.objects.pw_hash(request.POST['pw'])
        # create user
        if len(User.objects.all()) == 0:
            user = User.objects.create(
                f_name=request.POST['f_name'],
                l_name=request.POST['l_name'],
                email=request.POST['email'],
                user_level=9,
                pw_hash=pw_hash,
            )
        else:
            user = User.objects.create(
                f_name=request.POST['f_name'],
                l_name=request.POST['l_name'],
                email=request.POST['email'],
                user_level=1,
                pw_hash=pw_hash,
            )
        try:
            request.POST['admin_auth'] == "admin_auth"
        except:
            request.session['active_user_id'] = user.id
        return redirect('klaxonKitchen:home')

def confirm_delete(request, user_id):
    print(user_id)
    context = {
        "user_id": user_id
    }
    return render(request, 'login/confirm_delete.html', context)


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('login:login')
