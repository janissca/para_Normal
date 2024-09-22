import time
from django.utils import timezone
from datetime import datetime, timedelta

from kronaclub.celery import celery_app
from taskapp.bot import send_message_telegram
from taskapp.models import ScheduledTask
from eventsapp.models import (
    Event,
    Location,
    Attendee,
    ThemeOfEvent,
    EventTheme
)


def handle_event_created(user_id, event_id):
    event = Event.objects.get(id=event_id)
    user = event.host_id
    
    message = f"Здравствуйте, {user.first_name} {user.last_name}!\n Ваше заявка на мероприятие {event.name} отправлено на рассмотрение."
    celery_task = notify.apply_async((user.telegram_id, message), countdown=0)
    create_scheduled_task(celery_task.id, event, user, event.start_date)

    message = f"Здравствуйте, {user.first_name} {user.last_name}!\n Через 1.5 часа начнется мероприятие {event.name}."
    celery_task = notify.apply_async((user.telegram_id, message), eta=timezone.now() + time_until_event(event.start_date, 1.5))
    create_scheduled_task(celery_task.id, event, user, event.start_date)


def handle_event_updated(user_id, event_id):
    print(user_id, event_id)
    event = Event.objects.get(id=event_id)
    user = event.host_id

    message = f"Здравствуйте, {user.first_name} {user.last_name}!\n Ваша заявка на мероприятие {event.name} обновлена."
    celery_task = notify.apply_async((user.telegram_id, message), countdown=0)
    create_scheduled_task(celery_task.id, event, user, event.start_date)
    # send_message_telegram('477901815', 'Hello from the bot!')

    
    attendees = Attendee.objects.filter(event_id=event_id)
    for attendee in attendees:
        message = f"Здравствуйте, {attendee.user.first_name} {attendee.user.last_name}!\n Мероприятие {event.name} было изменено."
        celery_task = notify.apply_async((attendee.user.telegram_id, message), countdown=0)
        create_scheduled_task(celery_task.id, event_id, user_id, event.start_date)


def handle_event_deleted(user_id, event_id):
    event = Event.objects.get(id=event_id)
    user = event.host_id

    message = f"Здравствуйте, {user.first_name} {user.last_name}!\n Ваша заявка на мероприятие {event.name} отменена."
    celery_task = notify.apply_async((user.telegram_id, message), countdown=0)
    create_scheduled_task(celery_task.id, event, user, event.start_date)

    attendees = Attendee.objects.filter(event_id=event_id)
    for attendee in attendees:
        message = f"Здравствуйте, {attendee.user.first_name} {attendee.user.last_name}!\n Мероприятие {event.name} было отменено."
        celery_task = notify.apply_async((attendee.user.telegram_id, message), countdown=0)
        create_scheduled_task(celery_task.id, event, user, event.start_date)

    ScheduledTask.objects.filter(event_id=event_id).update(status='cancelled')


def handle_event_subscribed(user_id, event_id):
    event = Event.objects.get(id=event_id)
    user = event.host_id

    message = f"Здравствуйте, {user.first_name} {user.last_name}!\n Вы зарегистрированы на мероприятие {event.name}."
    celery_task = notify.apply_async((user.telegram_id, message), countdown=0)
    create_scheduled_task(celery_task.id, event, user, event.start_date)

    message = f"Здравствуйте, {user.first_name} {user.last_name}!\n Через 1.5 часа начнется мероприятие {event.name}."
    celery_task = notify.apply_async((user.telegram_id, message), eta=timezone.now() + time_until_event(event.start_date, 1.5))
    create_scheduled_task(celery_task.id, event, user, event.start_date)


def handle_event_unsubscribed(user_id, event_id):
    event = Event.objects.get(id=event_id)
    user = event.host_id

    message = f"Здравствуйте, {user.first_name} {user.last_name}!\n Вы отписались от мероприятия {event.name}."
    celery_task = notify.apply_async((user.telegram_id, message), countdown=0)
    create_scheduled_task(celery_task.id, event, user, event.start_date)
    ScheduledTask.objects.filter(event_id=event_id, user_id=user_id).update(status='cancelled')


@celery_app.task
def notify(telegram_login, message):
    send_message_telegram(telegram_login, message)


def cancel_task(celery_task_id):
    try:
        task = ScheduledTask.objects.get(celery_id=celery_task_id)
        celery_app.control.revoke(celery_task_id, terminate=True)
        task.status = 'cancelled'
        task.save()
    except ScheduledTask.DoesNotExist:
        pass


def create_scheduled_task(celery_id, event, user, start_date):
    task = ScheduledTask.objects.create(
        celery_id = celery_id,
        event_id = event,
        user_id = user,
        start_date = start_date,
    )
    task.save()


def update_scheduled_task(celery_id, event, user, start_date, status):
    task = ScheduledTask.objects.get(celery_id=celery_id)
    task.event_id = event
    task.user_id = user
    task.start_date = start_date
    task.status = status
    task.save()


def time_until_event(event_start_time, hours_before_event=1.5):
    current_time = timezone.now()
    
    if timezone.is_naive(event_start_time):
        event_start_time = timezone.make_aware(event_start_time)

    event_time = event_start_time - timedelta(hours=hours_before_event)
    time_remaining = event_time - current_time
    return time_remaining if time_remaining > timedelta(0) else timedelta(0)
# 