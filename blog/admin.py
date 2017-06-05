from django.contrib import admin

from .models import Text, Photo, Link
# Register your models here.
admin.site.register(Text)
admin.site.register(Photo)
admin.site.register(Link)
