from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from eventsapp.models import (
    Event,
    Location,
    Attendee,
    ThemeOfEvent,
    EventTheme
)
from taskapp.tasks import (
    handle_event_created,
    handle_event_updated,
    handle_event_deleted,
    handle_event_subscribed,
    handle_event_unsubscribed
)


@receiver(post_save, sender=Event)
def post_save_event(sender, instance, created, **kwargs):
    if created:
        handle_event_created(instance.host_id.id, instance.id)
    else:
        handle_event_updated(instance.host_id.id, instance.id)


@receiver(post_delete, sender=Event)
def post_delete_event(sender, instance, **kwargs):
    handle_event_deleted(instance.host_id.id, instance.id)


@receiver(post_save, sender=Attendee)
def post_save_attendee(sender, instance, created, **kwargs):
    handle_event_subscribed(instance.user_id.id, instance.event_id.id)


@receiver(post_delete, sender=Attendee)
def post_delete_attendee(sender, instance, **kwargs):
    handle_event_unsubscribed(instance.user_id.id, instance.event_id.id)
