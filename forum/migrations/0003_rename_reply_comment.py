# Generated by Django 5.0.1 on 2024-02-11 20:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_blog_options_alter_reply_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reply',
            new_name='Comment',
        ),
    ]
