from django.contrib import admin

from .models import FMCG,FB,Jewellery
# Register your models here.

class  AdminFmcg(admin.ModelAdmin):
    list_display=('Id','Title','Image')

class  AdminJewellery(admin.ModelAdmin):
    list_display=('Id','Title','Image')

class  AdminFb(admin.ModelAdmin):
    list_display=('Id','Title','Image')


admin.site.register(FMCG,AdminFmcg)
admin.site.register(Jewellery,AdminJewellery)
admin.site.register(FB,AdminFb)