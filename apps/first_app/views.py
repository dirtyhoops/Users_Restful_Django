from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

#GET route to render index.html
def index(request):
    users = Users.objects.all()
    return render(request, 'first_app/index.html', {"users": users})

#POST route for create user
def create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        Users.objects.create(first_name = first_name, last_name =last_name, email = email)
    return redirect('/')

#POST route for update user
def update(request, id):
    if request.method == 'POST':
        errors = Users.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/users/' + id + '/edit')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
        
            user = Users.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            messages.success(request, "User successfully updated")
    return redirect('/users/' + id)

#GET route for edit user
def edit(request, id):
    user = Users.objects.get(id = id)
    return render(request, 'first_app/edit.html', {"user": user})
    
#GET route for new user
def new(request):
    return render(request, 'first_app/new.html')

#GET route for show user
def show(request, id):
    user = Users.objects.get(id=id)
    return render(request, 'first_app/show.html', {"user" : user})

#GET route for destroy
def destroy(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('/')