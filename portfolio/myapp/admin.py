from django.contrib import admin
from myapp.models import contectEnquiry
# Register your models here.
class contectAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'subject' ,'message')

admin.site.register(contectEnquiry,contectAdmin)
# admin.site.register(contectAdmin)
# admin.site.register(contectEnquiry)
