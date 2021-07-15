from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserInformationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = UserInformationForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user_information = form2.save(commit=False)
            user_information.user = user
            user_information.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'account/signup.html', {'form1':form1, 'form2':form2})
        
    else:
        form1 = UserCreationForm()
        form2 = UserInformationForm()
        return render(request, 'account/signup.html', {'form1':form1, 'form2':form2})

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth.login(request,user)
            return redirect('main')
        else:
            return render(request, 'account/login.html', {'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'account/login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main')