# Generated by Django 3.1.2 on 2020-11-15 10:00
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0006_auto_20201115_0048"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="address",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                verbose_name="Место пропажи/находки",
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="description",
            field=models.CharField(max_length=5000, verbose_name="Описание"),
        ),
    ]