# Create your models here.
# author: liuchunzi

from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import SET_NULL, Sum
from django_mysql.models import JSONField, Model

from system_settings.common.model_utils import Char, Dtime, Bool, Text, ForeignKey, Dday, Integer, Float


class Writer(models.Model):
    """
    写作者的信息表，存储了作者的信息和作者所在的群组
    writer_id是每个作者的唯一id，也是user表中的id
    """
    reader_id = Integer()
    write_id = Integer(db_index=True)
    phone_num = Char(max_length=64, null=True, blank=True)
    ID_number = Char(max_length=256, null=True, blank=True)
    group_id = Char(max_length=1024, null=True, blank=True)
    write_experience = Integer(default=0, null=True, blank=True)
    write_level = Integer(default=0, null=True, blank=True)
    income_balance = Float(default=0, null=True, blank=True)
    income_total = Float(default=0, null=True, blank=True)
    # additional_id = Integer(null=True, blank=True)
    is_active = Bool(default=False)
    is_delete = Bool(default=False)

    def __str__(self):
        return str(self.write_id)


class Group(models.Model):
    """
    写作群的表，存储了各个写作群的信息
    """
    group_name = Char(max_length=64, db_index=True)
    group_member_id = Char(max_length=256, null=True, blank=True)
    group_level = Char(max_length=256, null=True, blank=True)
    group_experience = Integer(default=0, null=True, blank=True)
    group_mumber_number = Integer(default=0, null=True, blank=True)
    group_book_id = Char(max_length=256, null=True, blank=True)
    income_total = Float(default=0, null=True, blank=True)
    group_admin_id = Char(max_length=64, null=True, blank=True)
    additional_json = JSONField()
    # additional_id = Integer(null=True, blank=True)
    is_active = Bool(default=False)
    is_delete = Bool(default=False)

    def __str__(self):
        return self.group_name
