# Generated by Django 5.0.4 on 2024-05-15 11:35

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0016_alter_refreshtokenmodel_expires_at_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RefreshToken",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("token", models.CharField(max_length=255)),
                ("expiry_date", models.DateTimeField(default=datetime.datetime.now)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="refresh_token",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
