# Create your views here.
from django.template.response import TemplateResponse

from djangocrm.contacts.models import Contact
from djangocrm.shortcuts import r

def base(request):
    all_contacts = Contact.objects.all()
    template = 'contacts.html'
    return r(template,
            {'all_contacts': all_contacts},
            request)