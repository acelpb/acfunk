from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from imagekit.processors import SmartResize
from ordered_model.models import OrderedModel


class Artwork(OrderedModel):
    ABSTRACTS = 0
    IMPRESSIONS = 1
    BIRDS = 2
    PORTRAITS = 3

    TYPE_CHOICES = (
        (ABSTRACTS, 'Abstracts'),
        (IMPRESSIONS, 'Impressions'),
        (BIRDS, 'Birds'),
        (PORTRAITS, 'Portraits'),
    )

    picture = models.ImageField(upload_to='artwork')
    medium_thumbnail = ImageSpecField(source='picture',
                                      processors=[SmartResize(400, 400)],
                                      format='JPEG',
                                      options={'quality': 60})

    small_thumbnail = ImageSpecField(source='picture',
                                     processors=[ResizeToFit(100, 100)],
                                     format='JPEG',
                                     options={'quality': 60})

    title = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE_CHOICES, null=False)
    description = models.TextField(default="", blank=True)

    order_with_respect_to = ('type', )
