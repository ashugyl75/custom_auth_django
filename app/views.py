from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse

# Create your views here.

def signUp(request):
    # this function will serve two endpoints:
    # 1. When someone wants to access the sign up page (get request)
    # 2. other when someone wants to submit the sign up form
    
    User = get_user_model() # if we were using the in built user model then we could access it directly but now we need this method, which comes really handy to get a reference to the current user model being used
    
    # Logged-in user do not need to register a new account
    if request.user.is_authenticated:
        # replace the below line with where you want your user to be redirected if they are already logged in
        return render(request=request, template_name="home.html")

    # handle the form submission logic here
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        user = User.objects.create_user(username = username, email = email,
                                        password = password, dob = dob, gender = gender)
        
        # redirect the user to the home page
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user) # login the user so they do not have to re enter the same information again
        return redirect("/")
    
    # if we receive a get request
    return render(request=request, template_name="signUp.html", context={})

def signIn(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return HttpResponse("fail")

    return render(request=request, template_name="signIn.html", context={})


def home(request):
    return render(request=request, template_name="home.html", context={})


def signOut(request):
    if request.user.is_authenticated:    
        logout(request)
        return HttpResponse("<strong>logout successful.<a href='signIn'> Go to Login page</a></strong>")
    else:
        return HttpResponse("<strong>invalid request</strong>")