# Generated by Django 4.2.3 on 2023-08-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("realtorapp", "0003_product_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="house_for",
            field=models.TextField(
                blank=True,
                choices=[("Vecation", "Vecation"), ("Normal", "Normal")],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="sell_type",
            field=models.TextField(
                blank=True, choices=[("Sell", "Sell"), ("Rent", "Rent")], null=True
            ),
        ),
    ]
