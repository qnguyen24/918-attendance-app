from django.contrib import admin

from .models import Cadet, Day, Flight

class DayAdmin(admin.ModelAdmin):
	fieldsets = [
		('day info',       {'fields': ['date']}),
		('cadets present', {'fields': ['cadetsPresent']}),
	]

class FlightAdmin(admin.ModelAdmin):
	fieldsets = [
		('flight info', {'fields': ['name','nickname']}),
		('cadets', {'fields': ['cadets']}),
	]

admin.site.register(Cadet)
admin.site.register(Day, DayAdmin)
admin.site.register(Flight, FlightAdmin)