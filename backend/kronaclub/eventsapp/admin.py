from django.contrib import admin

from eventsapp.models import (
    Event,
    Location,
    Attendee,
    ThemeOfEvent,
    EventTheme
)


admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Attendee)
admin.site.register(ThemeOfEvent)
admin.site.register(EventTheme)
