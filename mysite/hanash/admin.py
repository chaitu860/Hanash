from django.contrib import admin
from .models import HanashUser,Room,Message,Comments,Posts
admin.site.register(HanashUser)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Comments)
admin.site.register(Posts)
# Register your models here.
