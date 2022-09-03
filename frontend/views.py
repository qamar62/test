from django.shortcuts import render

# Create your views here.


def mainSite(request):
    
    context = {}
    return render(request, 'frontend/seo.html', context)