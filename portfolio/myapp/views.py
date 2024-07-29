from django.http import HttpRequest
from django.shortcuts import render
from myapp.models import contectEnquiry
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request,'index.html')

# def send_email_to_admin(request):
#     subject="testing email"
#     message= 'vishal chouahn'
#     from_email=settings.EMIAL_HOST_USER
#     recipient_list=['vchouhan9131@gmail.com']
    
    # send_mail(subject,message,from_email,recipient_list)

def data_insert(request):
    # n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=contectEnquiry(name=name, email=email, subject=subject, message=message)
        en.save()
        # n="data inserted succesfully"
    return render(request,'index.html')
