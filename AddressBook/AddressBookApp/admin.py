# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Library, AddressBook, ContactCard

admin.site.register(Library)
admin.site.register(AddressBook)
admin.site.register(ContactCard)
