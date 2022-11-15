# Generated by Django 4.1.3 on 2022-11-15 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='slug',
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]