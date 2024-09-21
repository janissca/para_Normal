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
    # host_id = CustomUserSerializer()
    # location_id = LocationSerializer()
    # event_type_name = serializers.CharField(source='get_event_type_display')

    class Meta:
        model = Event
        fields = '__all__'
        # read_only_fields = ('id', 'host_id', 'event_type_name', 'location_id')

class EventDetailSerializer(serializers.ModelSerializer):
    host = CustomUserSerializer(source='host_id', many=False, required=False, read_only=True)
    # location = CustomUserSerializer(source='location_id', many=False, required=False, read_only=True)

    # host_id = CustomUserSerializer()
    # location_id = LocationSerializer()
    # event_type_name = serializers.CharField(source='get_event_type_display')
    # category = serializers.HyperlinkedRelatedField(
    #     view_name='api:productcategory-detail',
    #     lookup_field='pk',
    #     many=False,
    #     read_only=False,
    #     queryset=ProductCategory.objects.all())

    class Meta:
        model = Event
        fields = '__all__'
        # read_only_fields = ('id', 'host', 'event_type_name', 'location')



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
        
