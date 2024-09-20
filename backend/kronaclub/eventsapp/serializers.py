from rest_framework import serializers

from eventsapp.models import (
    Event,
    Location,
    Attendee,
    ThemeOfEvent,
    EventTheme
)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'  
    

class ThemeOfEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeOfEvent
        fields = '__all__'


class EventThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTheme
        fields = '__all__'
