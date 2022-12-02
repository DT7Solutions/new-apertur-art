from django.shortcuts import render,redirect
from .models import FMCG,Jewellery, FB,Banner_video,Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    sliding_item1 = FMCG.objects.all()
    sliding_item2 = Jewellery.objects.all()
    sliding_item3 = FB.objects.all()
    banner_video = Banner_video.objects.all()
    
    
    # Contact us  form submission  
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        
        oContactinfo = Contact(Name=name,Email=email,Subject=subject,Message=message)
        oContactinfo.save()
    
        sucess =f'hi {name} sucessfully Sending email'
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['aperturart@gmail.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'your emsil sending fail')

    # subscribe  form submission  
    if request.method == "POST":
        email = request.POST.get('email',"")
        sucess =f'hi {name} sucessfully Sending email'
        # message = 'subscribe'
        subject ="subscribe"
        try:
            send_mail(subject,'noreplaybadugudinesh94@gmail.com',recipient_list=['aperturart@gmail.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'your emsil sending fail')
    

    return render(request, 'uifiles/index.html',{'sliding_item1':sliding_item1,'sliding_item2':sliding_item2,'sliding_item3':sliding_item3,'banner_video':banner_video})

def page_not_found_view(request, exception):
    return render(request, 'uifiles/404.html', status=404)