# Generated by Django 5.0.4 on 2024-05-01 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_alter_refreshtokenmodel_expires_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="refreshtokenmodel",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 31, 21, 38, 48, 270128, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
