# Generated by Django 4.1.3 on 2022-11-22 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0010_schedule_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='has_schedule',
            field=models.BooleanField(default=False),
        ),
    ]
