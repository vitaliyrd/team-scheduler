from django.contrib import admin

from scheduler.models import Event, EventCategory, Role, RoleCategory, Position, User

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Position)
admin.site.register(Role)
admin.site.register(RoleCategory)
admin.site.register(User)
