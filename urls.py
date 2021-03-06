from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from djangocrm.base.views import Home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'', include('djangocrm.tweets.urls')),
    url(r'^$', Home.as_view(), name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/', include('djangocrm.contacts.urls')),
    
)
