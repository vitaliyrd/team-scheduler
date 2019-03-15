from enum import Enum

from django.db import models

from scheduler.models import base
from scheduler.models.member import Role, Member


class EventCategory(base.Category):
    class Meta:
        verbose_name_plural = 'Event categories'


class Event(base.Model):
    name = models.CharField(max_length=base.NAME_LENGTH)
    description = models.CharField(
        blank=True,
        max_length=base.DESCRIPTION_LENGTH,
    )
    category = models.ForeignKey(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        to=EventCategory,
    )
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.name


class Position(base.Model):
    class Status(Enum):
        ACCEPTED = 'Accepted'  # Member has accepted their invite for this position.
        DECLINED = 'Declined'  # Member has declined their invite for this position.
        PENDING = 'Pending'    # Member has been sent an invite, but has not yet responded.

    event = models.ForeignKey(
        on_delete=models.CASCADE,
        to=Event,
    )
    role = models.ForeignKey(
        on_delete=models.CASCADE,
        to=Role,
    )
    member = models.ForeignKey(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        to=Member,
    )
    status = models.CharField(
        blank=True,
        choices=[(status.name, status.value) for status in Status],
        max_length=max([len(status.name) for status in Status]),
        null=True,
    )

    def __str__(self):
        return '%s (%s)' % (self.role.name, self.event.name)
