import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection

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
    UserType
)


JSON_PATH = 'assets'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r',
              encoding='utf-8') as f:
        return json.load(f)


class Command(BaseCommand):
    help = 'Filling the database'

    def handle(self, *args, **options):
        users_data = loadFromJSON('users')
        typeofusers_data = loadFromJSON('type_of_user')
        usertypes_data = loadFromJSON('user_type')
        locations_data = loadFromJSON('locations')
        events_data = loadFromJSON('events')
        themeofevents_data = loadFromJSON('them_of_events')
        eventthemes_data = loadFromJSON('event_themes')
        attendees_data = loadFromJSON('attendees')
        
        Location.objects.all().delete()
        Event.objects.all().delete()
        Attendee.objects.all().delete()
        ThemeOfEvent.objects.all().delete()
        EventTheme.objects.all().delete()
        CustomUser.objects.all().delete()
        TypeOfUser.objects.all().delete()
        UserType.objects.all().delete()

        # for i in (
        #         'ALTER SEQUENCE eventsapp_location_id_seq RESTART WITH 1;',
        #         'ALTER SEQUENCE eventsapp_event_id_seq RESTART WITH 1;',
        #         'ALTER SEQUENCE eventsapp_attendee_id_seq RESTART WITH 1;',
        #         'ALTER SEQUENCE eventsapp_themeofevent_id_seq RESTART WITH 1;',
        #         'ALTER SEQUENCE eventsapp_eventtheme_id_seq RESTART WITH 1;',
        #         # 'ALTER SEQUENCE eventsapp_location_id_seq RESTART WITH 1;',
        # ):
        #     connection.cursor().execute(i)

        super_user = CustomUser.objects.create_superuser(
            'super@mail.ru',
            'super',
            '1995-12-12',
            'super'
        )

        for user_data in users_data:
            user = CustomUser(
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                date_of_birth=user_data['date_of_birth'],
                password=user_data['password'],
                telegram_login=user_data['telegram_login'],
                telegram_id=user_data['telegram_id'],
                phone_number=user_data['phone_number'],
            )
            user.save()

        for typeofuser_data in typeofusers_data:
            typeofuser = TypeOfUser(
                name=typeofuser_data['type_user'],
            )
            typeofuser.save()
        
        for usertype_data in usertypes_data:
            user = CustomUser.objects.get(email=usertype_data['user'])
            typeofuser = TypeOfUser.objects.get(name=usertype_data['type_of_user'])
            usertype = UserType(
                user=user,
                type_of_user=typeofuser,
            )
            usertype.save()

        for location_data in locations_data:
            location = Location(
                country=location_data['country'],
                region=location_data['region'],
                city=location_data['city'],
                address=location_data['address'],
                venue=location_data['venue'],
            )
            location.save()

        for event_data in events_data:
            host = CustomUser.objects.get(email=event_data['host_id'])
            location = Location.objects.get(venue=event_data['location_id'])

            event = Event(
                name=event_data['name'],
                description=event_data['description'],
                event_type=event_data['event_type'],
                start_date=event_data['start_date'],
                end_date=event_data['end_date'],
                host_id=host,
                location_id=location,
            )
            event.save()

        for themeofevent_data in themeofevents_data:
            themeofevent = ThemeOfEvent(
                theme=themeofevent_data['theme'],
            )
            themeofevent.save()

        for eventtheme_data in eventthemes_data:
            theme = ThemeOfEvent.objects.get(theme=eventtheme_data['theme_id'])
            event = Event.objects.get(name=eventtheme_data['event_id'])
            eventtheme = EventTheme(
                theme_id=theme,
                event_id=event,
            )
            eventtheme.save()

        for attendee_data in attendees_data:
            event = Event.objects.get(name=attendee_data['event_id'])
            user = CustomUser.objects.get(email=attendee_data['user_id'])

            attendee = Attendee(
                event_id=event,
                user_id=user,
            )
            attendee.save()
