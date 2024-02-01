# Generated by Django 4.1 on 2024-01-31 14:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vpn_service", "0002_redirection_visits"),
    ]

    operations = [
        migrations.RenameField(
            model_name="page",
            old_name="url",
            new_name="original_url",
        ),
        migrations.AlterUniqueTogether(
            name="page",
            unique_together={("original_url", "title", "user")},
        ),
        migrations.AddField(
            model_name="page",
            name="vpn_proxi",
            field=models.CharField(default="proxi", max_length=256),
            preserve_default=False,
        ),
    ]