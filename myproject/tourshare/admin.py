from django.contrib import admin

# Register your models here.
from .models import create_user,create_team,join_user,Room,Message

admin.site.register(create_user)
admin.site.register(create_team)
admin.site.register(join_user)
admin.site.register(Room)
admin.site.register(Message)
