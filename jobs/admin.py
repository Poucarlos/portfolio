from django.contrib import admin
from .models import Job
# Register your models here.
#the purpose of this file is to tell the admin is to let something show up in the admin page
admin.site.register(Job)#in this case models