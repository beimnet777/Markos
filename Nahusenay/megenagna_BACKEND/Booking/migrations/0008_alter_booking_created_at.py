# Generated by Django 4.1.1 on 2023-12-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Booking", "0007_booking_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
