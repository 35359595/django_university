# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-04 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('univer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cathedra',
            name='c_univer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='univer.University'),
        ),
        migrations.AddField(
            model_name='lector',
            name='l_cathedra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='univer.Cathedra'),
        ),
        migrations.AddField(
            model_name='lector',
            name='l_univer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='univer.University'),
        ),
    ]