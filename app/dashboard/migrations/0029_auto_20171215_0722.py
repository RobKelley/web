# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_auto_20171214_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='comments',
            new_name='comments_priv',
        ),
        migrations.AddField(
            model_name='tip',
            name='comments_public',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tip',
            name='from_email',
            field=models.CharField(default='', max_length=255),
        ),
    ]