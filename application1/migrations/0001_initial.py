# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2024-05-24 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=29)),
                ('esal', models.CharField(max_length=30)),
                ('design', models.CharField(max_length=40)),
            ],
        ),
    ]
