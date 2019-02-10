# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class GenericCollection(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=400)
	date_added = models.DateTimeField('date added')
	last_modified_date = models.DateTimeField('date modified')

class Library(GenericCollection):
	pass

class AddressBook(GenericCollection):
	member_of_library = models.ManyToManyField(Library)

class ContactCard(GenericCollection):
	member_of_book = models.ManyToManyField(AddressBook)

class ContactField(models.Model):
	def __str__(self):
		return self.field_name
	field_name = models.CharField(max_length=400)
	field_value = models.CharField(max_length=400)
	member_of_contact = models.ForeignKey(ContactCard, on_delete=models.CASCADE)