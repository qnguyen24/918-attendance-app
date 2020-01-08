from django.contrib import admin

from .models import Cadet, Day, Flight

class DayInLine(admin.TabularInline):
	model = Day.cadetsPresent.through

class CadetAdmin(admin.ModelAdmin):
	fieldsets = [
		('cadet info',       {'fields': ['lastName','firstName']}),
	]
	inlines = [
		DayInLine,
	]
	
class DayAdmin(admin.ModelAdmin):
	fieldsets = [
		('day info',       {'fields': ['dayName','date']}),
		('cadets present', {'fields': ['cadetsPresent']}),
	]

class FlightAdmin(admin.ModelAdmin):
	fieldsets = [
		('flight info', {'fields': ['name','nickname']}),
		('cadets', {'fields': ['cadets']}),
	]

admin.site.register(Cadet, CadetAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Flight, FlightAdmin)