from django.shortcuts import render
from .models import FMCG,Jewellery, FB,Banner_video
# Create your views here.
def home(request):
    sliding_item1 = FMCG.objects.all()
    sliding_item2 = Jewellery.objects.all()
    sliding_item3 = FB.objects.all()
    banner_video = Banner_video.objects.all()
    return render(request, 'uifiles/index.html',{'sliding_item1':sliding_item1,'sliding_item2':sliding_item2,'sliding_item3':sliding_item3,'banner_video':banner_video})