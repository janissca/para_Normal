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
    count_of_attendees = serializers.IntegerField(source='attendee.count', read_only=True)
    event_type_name = serializers.StringRelatedField(read_only=True)
    attendees_list = serializers.PrimaryKeyRelatedField(source='attendee', many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        ordering = ['start_date']

    # def perform_create(self, serializer):
    #     print(">>> ", self.request.data)
    #     super().perform_create(serializer)
    #     # product_by_size = get_object_or_404(ProductBySize, pk=self.request.data['product_by_size_id'])
    #     # basket_product = Basket.objects.filter(user=self.request.user, product_id=product_by_size).first()
    #     # if not basket_product:
    #     #     serializer.save(user=self.request.user, product=product_by_size)
    #     # else:
    #     #     basket_product.quantity += serializer.data['quantity']
    #     #     basket_product.save()
    
    # def perform_update(self, serializer):
    #     print(">>> ", self.request.data)
    #     super().perform_create(serializer)


class TypeOfEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


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

    class Meta:
        model = Attendee
        fields = '__all__'


class AttendeeDetailSerializer(serializers.ModelSerializer):
    event_id = EventSerializer()
    user_id = CustomUserSerializer()

    class Meta:
        model = Attendee
        fields = '__all__'


class AttendeeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendee
        fields = ['user_id']


class EventDetailSerializer(serializers.ModelSerializer):
    host = CustomUserSerializer(source='host_id', many=False, required=False, read_only=True)
    location = LocationSerializer(source='location_id', many=False, required=False, read_only=True)
    attendees_list = serializers.PrimaryKeyRelatedField(source='attendee', many=True, read_only=True)
    event_type_name = serializers.StringRelatedField(source='event_type.name', read_only=True)
    # attendees_list = AttendeeDetailSerializer(source='attendee', many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
