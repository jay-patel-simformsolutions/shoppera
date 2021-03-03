from django.contrib import admin
from administration.models import UserProfile
from django.contrib.auth.models import Group


# Register your models here

admin.site.site_header = 'Shoppera Admin'
admin.site.register(UserProfile)
admin.site.unregister(Group)