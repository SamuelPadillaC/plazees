from django.contrib import admin

from .models import Info
from .models import Point

admin.site.register(Info)
admin.site.register(Point)