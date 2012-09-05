from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'djangocrm.contacts.views.base', name='crm-base'),
                       
)