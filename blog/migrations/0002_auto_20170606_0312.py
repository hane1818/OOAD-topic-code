# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='blog_photo'),
        ),
    ]
