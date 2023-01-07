from django.shortcuts import get_object_or_404, render
from django.contrib.admin.forms import AdminAuthenticationForm
from foodTrackingSystem.forms import *
from django.core.exceptions import EmptyResultSet
from django.contrib.auth import authenticate, login
from foodTrackingSystem.models import Product

def custom_login(request):
    form = AdminAuthenticationForm()
    if request.method == "GET":
        print('custom login GET')
        # login page
        return render(request, 'admin/login.html', {'form': form})
    elif request.method == "POST":
        print('custom login POST')
        print('request.POST: ', request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to dashboard
            print("user")
            return render(request, 'admin/index.html', {})
        else:
            # Return an 'invalid login' error message.
            print("no user")
    # return render(request, 'admin/login.html', {'form': form})