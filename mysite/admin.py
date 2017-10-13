from django.contrib import admin
from mysite import models

class UserAdmin(admin.ModelAdmin):
    list_display=('name','email','password','enabled')
    #ordering = ('-pub_time',)
admin.site.register(models.User,UserAdmin)
