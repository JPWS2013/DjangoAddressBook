from django.urls import path

from . import views

urlpatterns = [
	path('<int:addressbook_id>/index/', views.listcontacts, name='listcontacts'),
]

