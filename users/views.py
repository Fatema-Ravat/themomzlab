from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import UserLoginForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        print(request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            login_user = authenticate(request,username=data['username'],password=data['password'])
            print(login_user)
            if login_user is not None:
                login(request,login_user)
                return HttpResponse("User logged in")
            else:
                return HttpResponse('Not a valid user')
        else:
            print(user_login_form.errors.as_data())
            print(user_login_form.errors)
            return HttpResponse('Form Data not valid')
        
    else:
        user_login_form = UserLoginForm()
        return render(request,'users/login.html',{'user_login_form':user_login_form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_login')
    else:
        return render(request,'users/logout.html',{})
