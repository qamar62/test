from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Contact
# Create your views here.


def portfolio(request):
    form = Contact()
    
    if request.method == 'POST':
        
        
        form.name =  request.POST['name']
        form.email =  request.POST['email']
        form.subject =  request.POST['subject']
        form.message =  request.POST['message']
        form.save()
        messages.success(request, "Message was sent successfully")
        return redirect('home')
  
    
    context = {'form':form}
    return render(request, 'portfolio/home.html', context)


    
