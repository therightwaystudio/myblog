# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstblog', '0010_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
