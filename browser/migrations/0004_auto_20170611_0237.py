# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-11 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_auto_20170610_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='fit',
            field=models.CharField(max_length=100, null=True),
        ),
    ]