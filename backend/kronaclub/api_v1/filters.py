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


# class CompanyIdFilter(filters.RangeFilter, filters.DateFilter):
#     pass


# class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
#     pass


# class CharInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass


# class StatisticCompany(filters.FilterSet):
#     company = NumberInFilter(field_name='ID', lookup_expr='in')
#     responsible = NumberInFilter(field_name='ASSIGNED_BY_ID__ID', lookup_expr='in')

#     sector = filters.CharFilter(lookup_expr="icontains")
#     region = filters.CharFilter()
#     source = filters.CharFilter()
#     requisite_region = filters.CharFilter()
#     requisites_city = filters.CharFilter()

#     number_employees = filters.RangeFilter()
#     REVENUE = filters.RangeFilter()
#     DATE_CREATE = filters.DateFromToRangeFilter()

#     # inn = filters.CharFilter(field_name='inn', lookup_expr="regex")
#     inn = filters.CharFilter(lookup_expr="regex")
#     # inn_empty = filters.CharFilter(field_name="inn", lookup_expr="isnull")
#     # inn = filters.CharFilter()

#     class Meta:
#         model = Company
#         fields = ["company", "ASSIGNED_BY_ID", "sector", "region", "source",
#                   "requisite_region", "requisites_city", "number_employees",
#                   "REVENUE", "DATE_CREATE", "inn", ]


# class StatisticCompanyByDirection(filters.FilterSet):
#     company = NumberInFilter(field_name='ID', lookup_expr='in')

#     class Meta:
#         model = Company
#         fields = ["company", ]


# class StatisticByDirection(filters.FilterSet):
#     direction = NumberInFilter(field_name='ID', lookup_expr='in')

#     class Meta:
#         model = Direction
#         fields = ["direction", ]