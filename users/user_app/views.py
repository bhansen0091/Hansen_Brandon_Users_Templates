from django.shortcuts import render, redirect
from .models import Users

def index(request):
    context = {
        "all_users": Users.objects.all(),
    }
    return render(request, "index.html", context)

def create_user(request):
    Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age'],
    )
    return redirect('/')

def delete_user(request, user_id):
    Users.objects.get(id=user_id).delete()
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')