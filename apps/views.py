from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from qrcode import *
import random
# Create your views here.


def generate_qr(request, data):
    img = qrcode.make(data)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response



# def qrCode(request):
#     if request.method == "POST":
#         Url = request.POST['url']
#         img = make(Url)
#         img_name = f'qrimg{random.randint(1, 1000)}.png'
#         img.save(settings.MEDIA_ROOT/img_name)
#         return render(request, 'apps/qrcode.html', {'img':img_name})
    
#     return render(request,'apps/qrcode.html')
        
