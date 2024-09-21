from django_filters import rest_framework as filters


from eventsapp.models import (
    Event,
    Location,
    Attendee,
    ThemeOfEvent,
    EventTheme
)
from users.models import (
    CustomUser,
    TypeOfUser,
)


class UserFilter(filters.FilterSet):
    type_user_id = filters.CharFilter(field_name='user_type__type_of_user')

    class Meta:
        model = CustomUser
        fields = ['type_user_id', 'email', 'telegram_login', 'type_user_id',]


class EventFilter(filters.FilterSet):
    type_event_id = filters.CharFilter(field_name="event_theme__theme_id")
    start_date = filters.DateTimeFromToRangeFilter()
    host_id = filters.NumberFilter()
    location_id = filters.NumberFilter()

    class Meta:
        model = Event
        fields = ['type_event_id', 'start_date', 'host_id', 'location_id']


class AttendeeFilter(filters.FilterSet):

    class Meta:
        model = Attendee
        fields = ['event_id', 'user_id']
