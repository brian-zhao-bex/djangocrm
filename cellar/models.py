import base64
from django.db import models

# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=45, null=True, default='null')
    year = models.CharField(max_length=45, null=True, default='null')
    grapes = models.CharField(max_length=45, null=True, default='null')
    country = models.CharField(max_length=45, null=True, default='null')
    region = models.CharField(max_length=45, null=True, default='null')
    picture = models.CharField(max_length=255, null=True, default='null')
    _data = models.TextField(db_column='description', blank=True)
    
    def set_data(self, description):
        self._data = base64.encodestring(description)
    
    def get_data(self):
        return base64.decodestring(self._data)
    
    description = property(get_data, set_data)
    
    
