# Generated by Django 5.1.3 on 2024-11-20 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tEvents', '0004_alter_comments_eventid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='isAttending',
        ),
    ]