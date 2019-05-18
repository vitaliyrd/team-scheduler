from django.db import models

NAME_LENGTH = 250
DESCRIPTION_LENGTH = 1000


class Model(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    # TODO: Created by field
    updated = models.DateTimeField(auto_now=True)
    # TODO: Updated by field


class Category(Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=NAME_LENGTH)
    description = models.CharField(
        blank=True,
        max_length=DESCRIPTION_LENGTH,
    )

    def __str__(self):
        return self.name
