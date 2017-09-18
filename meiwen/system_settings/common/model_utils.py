from django.db import models

Char = models.CharField
Dtime = models.DateTimeField
Text = models.TextField
Email = models.EmailField
Integer = models.IntegerField
ForeignKey = models.ForeignKey
Bool = models.BooleanField
Dday = models.DateField
Float = models.FloatField


PROJECT_ID_MAPPING = {
    'system_settings': 1
}

Success_dict = {'status': 1, 'message': ''}
Error_dict = lambda msg: {'status': 0, 'message': '%s'%str(msg)}