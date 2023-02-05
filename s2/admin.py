from django.contrib import admin
from django.db import models
from .models import post,User,Comments,enq,dem,cat

# Register your models here.
admin.site.register(post)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(enq)
admin.site.register(dem)
admin.site.register(cat)
class postadmin(admin.ModelAdmin):
    list_display=['id','post','Image','title','user']
class Useradmin(admin.ModelAdmin):
    list_display=['id','name','email','password']
class commentadmin(admin.ModelAdmin):
    list_display=['id','name','post','commets']
class enqadmin(admin.ModelAdmin):
    list_display=['id','ques','emailenq']
class dem(admin.ModelAdmin):
    list_display=['id','img']

class cat(admin.ModelAdmin):
    list_display=['id','category']
