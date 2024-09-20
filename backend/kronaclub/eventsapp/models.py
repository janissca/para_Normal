from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Location(models.Model):
    country = models.CharField(verbose_name='Страна', max_length=20)
    region = models.CharField(verbose_name='Регион', max_length=30)
    city = models.CharField(verbose_name='Город', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=50)
    venue = models.CharField(verbose_name='Место проведения', max_length=50)

    class Meta:
        verbose_name = 'Локация события'


class Event(models.Model):

    class EventType(models.TextChoices):
        PERSONAL_MEETING = 'PM', _('Индивидуальная встреча')
        ROUND_TABLE = 'RT', _('Круглый стол')
        INDUSTRY_TABLE = 'IT', _('Отраслевой стол')
        PUBLIC_EVENT = 'PI', _('Внешнее мероприятие')


    name = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=255)
    type = models.CharField(verbose_name='Тип события', max_length=2, choices=EventType.choices)
    start_date = models.DateTimeField(verbose_name='Дата и время начала')
    end_date = models.DateTimeField(verbose_name='Дата и время окончания')
    host_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

class ThemeOfEvent(models.Model):
    theme = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Тема событий'
        verbose_name_plural = 'Темы событий'


class EventTheme(models.Model):
    theme_id = models.ForeignKey(ThemeOfEvent, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    email = models.EmailField(verbose_name='e-mail')
    telegram_id = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Attendee(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# class TypeOfUser(models.Model):
#     type = models.CharField(verbose_name='Тип пользователя', max_length=20)


# class UserType(models.Model):
#     # user_id = models.ForeignKey('User', on_delete=models.CASCADE)
#     type_id = models.ForeignKey(TypeOfUser, on_delete=models.CASCADE)
