from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("all_blogs")
        else:
            messages.info(request, "Username Or Password is incorrect")   
        

    
    context = {}
    return render(request, 'registration/login.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('login')