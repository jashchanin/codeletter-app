# Generated by Django 4.1.4 on 2023-01-05 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_notification_post_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="post_slug",
        ),
    ]
