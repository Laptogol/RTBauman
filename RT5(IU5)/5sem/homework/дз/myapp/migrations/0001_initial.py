# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('idconcert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Concert')),
            ],
        ),
    ]
