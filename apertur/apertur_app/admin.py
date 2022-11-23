from django.contrib import admin

from .models import FMCG,FB,Jewellery,Banner_video
# Register your models here.
class  AdminBanner_video(admin.ModelAdmin):
    list_display=('Id','Title','Video')

class  AdminFmcg(admin.ModelAdmin):
    list_display=('Id','Title','Image')

class  AdminJewellery(admin.ModelAdmin):
    list_display=('Id','Title','Image')

class  AdminFb(admin.ModelAdmin):
    list_display=('Id','Title','Image')

admin.site.register(Banner_video,AdminBanner_video)

admin.site.register(FMCG,AdminFmcg)
admin.site.register(Jewellery,AdminJewellery)
admin.site.register(FB,AdminFb)