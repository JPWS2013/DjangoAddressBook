from django.urls import path

from . import views

urlpatterns = [
	path('<int:contactcard_id>', views.showcard, name='showcard'),
]