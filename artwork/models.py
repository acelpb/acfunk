from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize


class Artwork(models.Model):
    PAINTING = 0
    ETUDE = 1
    SKETCH = 2
    TYPE_CHOICES = (
        (PAINTING, 'Painting'),
        (ETUDE, 'Étude'),
        (SKETCH, 'Sketch'),
    )

    picture = models.ImageField(upload_to='artwork')
    thumbnail = ImageSpecField(source='picture',
                               processors=[SmartResize(400, 400)],
                               format='JPEG',
                               options={'quality': 60})
    title = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES, null=False)
