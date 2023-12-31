# Generated by Django 4.1.1 on 2023-11-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Room", "0002_roomprofile_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="roomprofile", old_name="status", new_name="availability_status",
        ),
        migrations.AddField(
            model_name="roomprofile",
            name="price",
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
