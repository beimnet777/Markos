# Generated by Django 4.1.1 on 2023-11-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Booking", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="total_amount",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
