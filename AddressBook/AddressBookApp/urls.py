from django.urls import include, path

# from . import views

urlpatterns = [
	path('Library/', include('AddressBookApp.Library.urls')),
    path('AddressBook/', include('AddressBookApp.AddressBook.urls')),
    path('ContactCard/', include('AddressBookApp.ContactCard.urls')),
]