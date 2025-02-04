# Generated by Django 4.2.13 on 2024-05-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_customer_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="branch",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Ortigas Avenue", "Ortigas Avenue"),
                    ("Shangri-La Plaza", "Shangri-La Plaza"),
                    ("Katipunan Avenue", "Katipunan Avenue"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
