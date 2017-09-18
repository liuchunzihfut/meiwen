from django.db import models

# Create your models here.

from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import SET_NULL, Sum
from django_mysql.models import JSONField, Model

from system_settings.common.model_utils import Char, Dtime, Bool, Text, ForeignKey, Dday, Integer, Float


class reader(models.Model):
    """
    读者表，记录读者的信息
    """
    id = Char(max_length=255, null=True, db_index=True,)