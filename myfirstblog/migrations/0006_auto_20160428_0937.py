# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 09:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstblog', '0005_article_date_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_now',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 28, 9, 37, 12, 960089)),
        ),
    ]
