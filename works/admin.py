from django.contrib import admin
from . models import Project, Appeal


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'title',
            'description',
            'image',
            'link',
    )


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'name',
            'email',
            'message',
    )
