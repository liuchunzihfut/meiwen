# from django.db import models

# # Create your models here.

# from __future__ import unicode_literals
# import datetime

# from django.db import models
# from django.contrib.auth.models import User, Group
# from django.db.models import SET_NULL, Sum
# from django_mysql.models import JSONField, Model

# from system_settings.common.model_utils import Char, Dtime, Bool, Text, ForeignKey, Dday, Integer, Float


# class Reader(models.Model):
#     """
#     读者表，记录读者的信息
#     reader_id是每一个读者的唯一编号
#     vip_level为0时，代表读者不是vip
#     reader_id就是User表的id
#     """
#     reader_id = Char(max_length=255, db_index=True)
#     write_id = Char(max_length=255, default=null, null=True, blank=True)
#     nickname = Char(max_length=63, null=True, blank=True)
#     name = Char(max_length=63, null=True, blank=True)
#     gender = Char(max_length=63, null=True, blank=True)
#     experience = Integer(default=0, null=True, blank=True)
#     level = Integer(default=0, null=True, blank=True)
#     vip_level = Integer(default=0, null=True, blank=True)
#     account_balance = Float(default=0, null=True, blank=True)
#     birthday = Dday(null=True, blank=True)
#     additional_id = Integer(null=True, blank=True)
#     is_active = Bool(default=False, null=True, blank=True)
#     is_delete = Bool(default=False, null=True, blank=True)

#     def __str__(self):
#         return self.reader_id