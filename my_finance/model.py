# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Expense(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'expense'

    def __str__(self):
        return self.name

class ExpenseOperation(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    expense = models.ForeignKey(Expense, models.DO_NOTHING, db_column='expense')
    description = models.CharField(max_length=50)
    balance = models.FloatField(blank=True, null=True)
    operation_date = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_operation'

    def __str__(self):
        return self.expense.name+" - "+self.description+" - "+str(self.balance)

class Ingress(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ingress'

    def __str__(self):
        return self.name


class IngressOperation(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    ingress = models.ForeignKey(Ingress, models.DO_NOTHING, db_column='ingress')
    description = models.CharField(max_length=100)
    balance = models.FloatField(blank=True, null=True)
    operation_date = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingress_operation'

    def __str__(self):
        return self.ingress.name + " - " + self.description + " - " + str(self.balance)



