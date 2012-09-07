from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    ('^names$', 'names.views.index'),
    ('^names\/1$', 'names.views.edit'),
    ('^templates\/index$', 'names.views.index_template'),
    ('^templates\/edit$', 'names.views.edit_template'),                       
)