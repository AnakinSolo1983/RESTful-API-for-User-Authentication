# Generated by Django 5.0.4 on 2024-04-29 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_refreshtokenmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="refreshtokenmodel",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 29, 19, 33, 22, 374800, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]