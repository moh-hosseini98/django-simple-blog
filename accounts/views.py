from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages


from .forms import CreateUserForm

def register(request):
    
    form = CreateUserForm(request.POST or None)


    if request.method == 'POST':
        

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('accounts:login')


    context = {
        "form":form
    }        

    return render(request,'accounts/register.htm',context) 

def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home') 

        else:

            messages.error(request,'username or password is incorrect')
           
    form = AuthenticationForm()
    context = {
        "form":form
    }
    return render(request,'accounts/login.htm',context)      

def logoutuser(request):
    logout(request)
    return redirect('home')    