from contacts.models import Contact, hyperlink, Country, ContactAddress 
from django.contrib import admin

admin.site.register(Contact)
admin.site.register(hyperlink)
admin.site.register(Country)
admin.site.register(ContactAddress)