# Generated by Django 2.1.4 on 2019-01-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='type',
            field=models.IntegerField(choices=[(0, 'Painting'), (1, 'Étude'), (2, 'Sketch')]),
        ),
    ]
