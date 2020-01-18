from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Todo
# Register your models here.

admin.site.site_header = "Administrator"
admin.site.site_title = "Site Administration"
admin.site.index_title = "Dashboard"

admin.site.register(Todo)
admin.site.unregister(Group)


class TodoAdmin(admin.ModelAdmin):
    list_display = ('text', )
    list_filter = ('current_date', )