from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Artwork


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='small_thumbnail')

    list_filter = ('type',)
