# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(db_index=True, max_length=256)),
                ('book_group_id', models.CharField(max_length=256)),
                ('book_content_id', models.CharField(blank=True, max_length=64, null=True)),
                ('book_introduction', models.TextField(blank=True, null=True)),
                ('book_outline', models.TextField(blank=True, null=True)),
                ('book_chapter_num', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField(db_index=True)),
                ('chapter_id', models.IntegerField()),
                ('chapter_name', models.CharField(blank=True, max_length=64, null=True)),
                ('chapter_content', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
