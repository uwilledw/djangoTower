# Generated by Django 5.1.2 on 2024-10-17 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('coverImg', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=300)),
                ('capacity', models.IntegerField()),
                ('startDate', models.DateTimeField()),
                ('isCanceled', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, choices=[('concert', 'Concert'), ('convetion', 'Convetion'), ('sport', 'Sport'), ('digital', 'Digital')], max_length=10)),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('isAttending', models.BooleanField()),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tEvents.tevent')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPremium', models.BooleanField(default=False)),
                ('tEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tEvents.tevent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
