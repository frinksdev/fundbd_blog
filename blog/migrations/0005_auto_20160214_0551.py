# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_youvid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='youvid',
            field=models.URLField(blank=True),
        ),
    ]
