from django.contrib import admin
from django.conf import settings
from .models import Scooter, ScooterActivity

class ScooterActivityInline(admin.TabularInline):
    model = ScooterActivity

class ScooterAdmin(admin.ModelAdmin):
    readonly_fields = ('updated','created',)
    inlines = [ScooterActivityInline,]
    list_display = ('scooter_id','get_activity_count', 'distance_travelled',)
    ordering = ('-distance_travelled',)

    def get_activity_count(self, obj):
        return obj.scooteractivity_set.all().count()

    get_activity_count.short_description = 'Log points'

    class Media:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )
class ScooterActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('updated','created',)


admin.site.register(Scooter, ScooterAdmin)
admin.site.register(ScooterActivity, ScooterActivityAdmin)