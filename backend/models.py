from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):

    class EventType(models.TextChoices):
        PERSONAL_MEETING = 'PM', _('Индивидуальная встреча')
        ROUND_TABLE = 'RT', _('Круглый стол')
        INDUSTRY_TABLE = 'IT', _('Отраслевой стол')
        PUBLIC_EVENT = 'PI', _('Внешнее мероприятие')

    name = models.CharField(verbose_name='Название мероприятия', max_length=100)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=EventType.choices)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    host_id = models.ForeignKey('User', on_delete=models.CASCADE)
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE)
    


class Location(models.Model):
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)


class EventTheme(models.Model):
    theme_id = models.ForeignKey('ThemeOfEvent', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)


class ThemeOfEvent(models.Model):
    theme = models.CharField(max_length=20)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(default=None, null=True)
    telegram_id = models.IntegerField(max_length=6, unique=True)


class Attendee(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)


class UserType(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    type_id = models.ForeignKey('TypeOfUser', on_delete=models.CASCADE)


class TypeOfUser(models.Model):
    type = models.CharField(max_length=20)
