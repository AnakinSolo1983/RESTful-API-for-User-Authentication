# Generated by Django 5.0.4 on 2024-04-30 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_alter_refreshtokenmodel_expires_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="refreshtokenmodel",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 30, 18, 30, 20, 899341, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]