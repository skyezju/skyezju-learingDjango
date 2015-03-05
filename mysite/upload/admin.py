from django.contrib import admin
from upload.models import viewNavigation,uploadfromfile
# Register your models here.


class viewNavigationAdmin(admin.ModelAdmin):
    list_display = ('viewNavigation_text','viewID')


admin.site.register(viewNavigation,viewNavigationAdmin)
admin.site.register(uploadfromfile)