# Generated by Django 4.1.1 on 2023-10-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Room", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="roomprofile",
            name="image",
            field=models.ImageField(default=None, upload_to="room_image/"),
            preserve_default=False,
        ),
    ]