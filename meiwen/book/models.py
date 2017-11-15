# Create your models here.
# author: liuchunzi

from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import SET_NULL, Sum
from django_mysql.models import JSONField, Model

from system_settings.common.model_utils import Char, Dtime, Bool, Text, ForeignKey, Dday, Integer, Float


class Book(models.Model):
    """
    每本书的基本信息，包括书的名字，作者，简介，大纲，章节数
    """
    book_name = Char(max_length=256, db_index=True)
    book_group_id = Char(max_length=256)
    book_content_id = Char(max_length=64, null=True, blank=True)
    book_introduction = Text(blank=True, null=True)
    book_outline = Text(blank=True, null=True)
    book_chapter_num = Integer(default=0)
    is_completed = Bool(default=False)
    is_active = Bool(default=False)
    is_delete = Bool(default=False)

    def __str__(self):
        return self.book_name

class Content(models.Model):
    """
    书的章节内容
    """
    book_id = Integer(db_index=True)
    chapter_id = Integer()
    chapter_name = Char(max_length=64, null=True, blank=True)
    chapter_content = Text(blank=True, null=True)
    is_active = Bool(default=False)
    is_delete = Bool(default=False)

    def __str__(self):
        return str(self.book_id)

