# Generated by Django 5.1.3 on 2024-11-20 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tEvents', '0003_remove_comments_tevent_comments_eventid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='eventId',
            field=models.IntegerField(),
        ),
    ]