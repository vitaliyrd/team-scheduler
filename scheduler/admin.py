from django.contrib import admin

from scheduler.models import Event, EventCategory, Role, RoleCategory, Member, Position

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Member)
admin.site.register(Position)
admin.site.register(Role)
admin.site.register(RoleCategory)
