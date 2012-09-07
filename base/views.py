# Create your views here.
from django.template import Context, loader
from django.template.response import TemplateResponse
from django.views.generic import View

from djangocrm.shortcuts import r


class Home(View):
    def dispatch(self, *args, **kwargs):
        return super(Home, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.get_home_page(request, *args, **kwargs)
    
    def get_home_page(self, request, *args, **kwargs):
        template = 'wine.html'
        return r(template, {}, request)
    