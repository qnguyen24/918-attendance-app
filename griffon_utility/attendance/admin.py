from django.contrib import admin

from .models import Cadet, Day, Flight

admin.site.register(Cadet)
admin.site.register(Day)
admin.site.register(Flight)