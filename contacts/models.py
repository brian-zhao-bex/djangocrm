from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    birthday = models.DateField('Birthday')
    email = models.CharField(max_length=200)
    email_second = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200) 
    twitter = models.CharField(max_length=200)
    blog = models.CharField(max_length=200)


class hyperlink(models.Model):
    contact = models.ForeignKey(Contact)
    description = models.CharField(max_length=200, verbose_name=_('Description'))
    hyper_link = models.CharField(max_length=200, verbose_name=_('Links'))

class Country(models.Model):
    name = models.CharField(max_length=50)

class ContactAddress(models.Model):
    STATE_CHOICES = (
        ('NSW', 'New South Wales'),
        ('VIC', 'Victoria'),
        ('QLD', 'Queensland'),
        ('ACT', 'Australian Capital Territory'),
        ('SA', 'South Australia'),
        ('NT', 'Northern Territory'),
        ('WA', 'Western Australia'),
        ('TAS', 'Tasmania')
    )
    
    address_title = models.CharField(max_length=16, verbose_name=_('Address ID'), help_text=_('Example: Home or Office'))
    first_name = models.CharField(max_length=50, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    company = models.CharField(max_length=64, verbose_name=_('Company'), blank=True, null=True)
    address1 = models.CharField(max_length=64, verbose_name=_('Address Line 1'))
    address2 = models.CharField(max_length=64, verbose_name=_('Address Line 2'), blank=True, null=True)
    suburb = models.CharField(max_length=128, verbose_name=_('Suburb'))
    state = models.CharField(max_length=3, verbose_name=_('State'), choices=STATE_CHOICES, blank=True, null=True)
    postcode = models.CharField(max_length=4, verbose_name=_('Postal Code'))
    phone = models.CharField(max_length=32, verbose_name=_("Phone"), help_text=_("Example: 0280064346"))
    is_active = models.BooleanField(default=True)  # Can be set to False if a user "deletes" their address
    country = models.ForeignKey(Country, default='Australia')
    region = models.CharField(max_length=128, verbose_name=_('Town/City'), blank=True, null=True)
    contact = models.ForeignKey(Contact)