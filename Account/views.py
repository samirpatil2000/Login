from django.shortcuts import render,redirect

from.forms import userRegisterFrom
from django.contrib.auth.models import User


def home(request):
    return render(request,'Account/account_home.html')
def register(request):


    if request.user.is_authenticated:
        return redirect('home')

    register_form=userRegisterFrom()
    if request.method=="POST":
        register_form=userRegisterFrom(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            return redirect('home')

    context={
        'registerForm':register_form
    }
    return render(request,'Account/account_register.html',context)

