# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader

from ..models import ContactCard

def showcard(request, contactcard_id):
	card=ContactCard.objects.get(id=contactcard_id)
	template = loader.get_template('ContactCard/detailview.html')
	# str_last_modified_date = str(card.last_modified_date)

	context = {
		'card':card
	}

	return HttpResponse(template.render(context, request))

#It was last modified on %s.
#, str_last_modified_date