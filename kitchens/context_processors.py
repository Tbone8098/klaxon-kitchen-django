from django.shortcuts import render, redirect, HttpResponse
from login.models import *


def global_context(request):
    try:
        activeUserId = request.session["active_user_id"]
        activeUser = User.objects.get(id=activeUserId)
        conext = {
            'activeUser': activeUser
        }
        return conext
    except: 
        # return redirect('login:login')
        return HttpResponse("02")