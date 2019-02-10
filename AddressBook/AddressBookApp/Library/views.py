# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader

from ..models import Library, AddressBook

def listbooks(request):
	lib=Library.objects.get(id=2)
	addressbook_list = AddressBook.objects.filter(member_of_library=lib)
	template = loader.get_template('Library/index.html')
	context = {
		'addressbook_list':addressbook_list,
		'library_name':lib.name
	}
	return HttpResponse(template.render(context, request))