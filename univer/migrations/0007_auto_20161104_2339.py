# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-04 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univer', '0006_cathedra_cat_univer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='u_city',
            field=models.CharField(max_length=50),
        ),
    ]
