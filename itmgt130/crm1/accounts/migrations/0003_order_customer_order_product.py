# Generated by Django 4.2.13 on 2024-05-16 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_order_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.customer",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.product",
            ),
        ),
    ]
