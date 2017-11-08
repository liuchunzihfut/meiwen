# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(db_index=True, max_length=64)),
                ('group_member_id', models.CharField(blank=True, max_length=256, null=True)),
                ('group_level', models.CharField(blank=True, max_length=256, null=True)),
                ('group_experience', models.IntegerField(blank=True, default=0, null=True)),
                ('group_mumber_number', models.IntegerField(blank=True, default=0, null=True)),
                ('group_book_id', models.CharField(blank=True, max_length=256, null=True)),
                ('income_total', models.FloatField(blank=True, default=0, null=True)),
                ('group_admin_id', models.CharField(blank=True, max_length=64, null=True)),
                ('additional_json', django_mysql.models.JSONField(default=dict)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_id', models.IntegerField()),
                ('write_id', models.IntegerField(db_index=True)),
                ('phone_num', models.CharField(blank=True, max_length=64, null=True)),
                ('ID_number', models.CharField(blank=True, max_length=256, null=True)),
                ('group_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('write_experience', models.IntegerField(blank=True, default=0, null=True)),
                ('write_level', models.IntegerField(blank=True, default=0, null=True)),
                ('income_balance', models.FloatField(blank=True, default=0, null=True)),
                ('income_total', models.FloatField(blank=True, default=0, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
