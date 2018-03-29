# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AveenoDataException(models.Model):
    barcode = models.CharField(max_length=50, blank=True, null=True)
    sku_name = models.CharField(max_length=50, blank=True, null=True)
    wcc_id = models.CharField(max_length=50, blank=True, null=True)
    packagecode = models.CharField(max_length=50, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aveeno_data_exception'
        app_label = 'data_web'
