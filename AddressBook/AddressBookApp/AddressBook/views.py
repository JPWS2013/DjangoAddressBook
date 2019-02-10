# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader

from ..models import AddressBook, ContactCard

def listcontacts(request, addressbook_id):
	book = AddressBook.objects.get(id=addressbook_id)
	contact_list = ContactCard.objects.filter(member_of_book=book)
	template = loader.get_template('AddressBook/index.html')
	context = {
		'contact_list':contact_list,
		'book_name':book.name
	}
	return HttpResponse(template.render(context, request))
