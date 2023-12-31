# Generated by Django 4.1.1 on 2023-11-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Room", "0006_rename_status_roomprofile_availability_status_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                ("room_profile", models.ManyToManyField(to="Room.roomprofile")),
            ],
        ),
    ]
