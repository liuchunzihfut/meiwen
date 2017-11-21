# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(db_index=True)),
                ('group_id', models.IntegerField()),
                ('apply_type', models.CharField(blank=True, max_length=256, null=True)),
                ('apply_status', models.CharField(blank=True, max_length=256, null=True)),
                ('apply_message', models.CharField(blank=True, max_length=256, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]