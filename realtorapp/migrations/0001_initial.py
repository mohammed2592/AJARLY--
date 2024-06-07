# Generated by Django 4.2.3 on 2023-08-05 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="profile",
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
                ("phone", models.CharField(blank=True, max_length=11, null=True)),
                ("email", models.EmailField(blank=True, max_length=50, null=True)),
                ("address", models.CharField(blank=True, max_length=80, null=True)),
                ("f_name", models.CharField(blank=True, max_length=10, null=True)),
                ("L_name", models.CharField(blank=True, max_length=10, null=True)),
                ("picture", models.FileField(blank=True, null=True, upload_to="")),
                (
                    "country",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("Egypt", "Egypt"),
                            ("Canada", "Canada"),
                            ("USA", "USA"),
                            ("UAE", "UAE"),
                            ("KSA", "KSA"),
                            ("UK", "UK"),
                            ("Germany", "Germany"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
