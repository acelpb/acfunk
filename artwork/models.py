from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from imagekit.processors import SmartResize
from ordered_model.models import OrderedModel


class Artwork(OrderedModel):
    PAINTING = 0
    ETUDE = 1
    SKETCH = 2
    TYPE_CHOICES = (
        (PAINTING, 'Painting'),
        (ETUDE, 'Étude'),
        (SKETCH, 'Sketch'),
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
