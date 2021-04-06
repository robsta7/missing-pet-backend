# Generated by Django 3.1.2 on 2021-04-06 16:41
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0002_passwordresetconfirmationcode"),
    ]

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "settings_name",
                    models.CharField(
                        max_length=200,
                        unique=True,
                        verbose_name="Уникальное название настроек",
                    ),
                ),
                (
                    "actual_app_version_ios",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Актуальная версия приложения для ios",
                    ),
                ),
                (
                    "min_app_version_ios",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Минимальная версия приложения для ios",
                    ),
                ),
            ],
            options={
                "verbose_name": "Настройки",
                "verbose_name_plural": "Настройки",
            },
        ),
    ]