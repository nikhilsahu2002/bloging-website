from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout 
from django.contrib import messages,auth
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

# Create your views here.
def reg(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'Registration.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                user.save()
                return HttpResponse("User Is exist")
        else:
            return render (request,'Registration.html', {'error':'Password does not match!'})
    else:
        return render(request,'Registration.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/Login/')


@login_required
def restricted_page(request):
    return render(request, 'restricted.html')

