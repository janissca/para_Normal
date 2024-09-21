from rest_framework import serializers
from eventsapp.models import (
    Event,
    Location,
    Attendee,
    ThemeOfEvent,
    EventTheme
)
from users.serializers import CustomUserSerializer


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    host_id = CustomUserSerializer()
    location_id = LocationSerializer()
    event_type_name = serializers.CharField(source='get_event_type_display')

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'host_id', 'event_type_name', 'location_id')


class ThemeOfEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThemeOfEvent
        fields = '__all__'


class EventThemeSerializer(serializers.ModelSerializer):
    theme_id = ThemeOfEventSerializer()
    event_id = EventSerializer()

    class Meta:
        model = EventTheme
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    event_id = EventSerializer()
    user_id = CustomUserSerializer()

    class Meta:
        model = Attendee
        fields = '__all__'
        
