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
        verbose_name_plural = 'Локации событий'

    def __str__(self) -> str:
        return self.venue


class Event(models.Model):
    class EventType(models.TextChoices):
        PERSONAL_MEETING = 'PM', _('Индивидуальная встреча')
        ROUND_TABLE = 'RT', _('Круглый стол')
        INDUSTRY_TABLE = 'IT', _('Отраслевой стол')
        PUBLIC_EVENT = 'PI', _('Внешнее мероприятие')

    name = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=255)
    event_type = models.CharField(verbose_name='Тип события', max_length=2, choices=EventType.choices)
    start_date = models.DateTimeField(verbose_name='Дата и время начала')
    end_date = models.DateTimeField(verbose_name='Дата и время окончания')
    host_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    def __str__(self) -> str:
        return self.name


class ThemeOfEvent(models.Model):
    theme = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Тема событий'
        verbose_name_plural = 'Темы событий'

    def __str__(self) -> str:
        return self.theme


class EventTheme(models.Model):
    theme_id = models.ForeignKey(ThemeOfEvent, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тема события'
        verbose_name_plural = 'Темы событий'
    
    def __str__(self) -> str:
        return f"{self.event_id.id}. {self.event_id.name} - {self.theme_id.theme}"


class Attendee(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Участник события'
        verbose_name_plural = 'Участники события'
    
    def __str__(self) -> str:
        return f"{self.event_id.id}. {self.event_id.name}  - {self.user_id.first_name} - {self.user_id.last_name}"
