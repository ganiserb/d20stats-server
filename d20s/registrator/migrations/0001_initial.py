# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('roll', models.PositiveSmallIntegerField(help_text='The number rolled on the d20 dice', verbose_name='roll number')),
                ('moment_rolled', models.DateTimeField(auto_now_add=True, help_text='The moment the roll was registered')),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL, help_text='The player that made the roll')),
            ],
        ),
    ]
