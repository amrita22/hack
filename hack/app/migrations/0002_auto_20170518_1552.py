# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackdata',
            name='genre',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='hackdata',
            name='problem_statement',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='hackdata',
            name='identifier',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
