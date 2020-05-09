from django.contrib import admin
from main.models import Event, Category
from django.contrib.auth.models import Group


@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'community', 'venue', 'date', 'featured')
    list_filter = ('featured', 'date', 'community')


admin.site.register(Category)
admin.site.unregister(Group)
