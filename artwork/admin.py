from django.contrib import admin
from imagekit.admin import AdminThumbnail
from ordered_model.admin import OrderedModelAdmin

from .models import Artwork


@admin.register(Artwork)
class ArtworkAdmin(OrderedModelAdmin):
    list_display = ('title', 'type', 'admin_thumbnail', 'move_up_down_links')
    admin_thumbnail = AdminThumbnail(image_field='small_thumbnail')

    list_filter = ('type',)
