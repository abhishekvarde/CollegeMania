from django.contrib import admin
from .models import *
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.

admin.site.register(Campus)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Conversation)
admin.site.register(Message)

TokenAdmin.raw_id_fields = ['user']
