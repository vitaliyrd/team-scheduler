from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from scheduler.models import base


class RoleCategory(base.Category):
    class Meta:
        verbose_name_plural = 'Role categories'


class Role(base.Model):
    name = models.CharField(max_length=base.NAME_LENGTH)
    description = models.CharField(
        blank=True,
        max_length=base.DESCRIPTION_LENGTH,
    )
    category = models.ForeignKey(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        to=RoleCategory,
    )

    def __str__(self):
        return self.name


class Member(base.Model):
    user = models.OneToOneField(
        on_delete=models.CASCADE,
        to=User,
    )
    phone_number = PhoneNumberField(blank=True)
    roles = models.ManyToManyField(to=Role)

    def __str__(self):
        return self.user.get_full_name() or self.user.username