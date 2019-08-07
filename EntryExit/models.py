from django.db import models
import uuid
import datetime

 class Entry_Exit(models.Model):
     name = models.ForeignKey(blank=True, null=True)
     id =  models.IntegerField(blank=True, null=True)
     age = models.IntegerField(blank=True, null=True)
     dob = models.DateField(_("Date"))
     gate_entry_number = models.IntegerField(blank=True, null=True)
     entry_timestamp = models.DateTimeField(blank=True, null=True)
     exit_timestamp = models.DateTimeField(blank=True, null=True)

     def __str__(self):
         return self.name

    class Meta:
        verbose_name = "Entry Exit"
        verbose_name_plural = "Entry Exit"
