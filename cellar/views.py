from django import http
import pystache
import settings
import templates
 
pystache.View.template_path = settings.TEMPLATE_DIRS
 
 
def index(request):
    outline_template = templates.Outline()
    index_template = templates.Index()
    index_template.set_names([{
        'id': '1',
        'name': 'Joe',
        }])
    outline_template.set_body(index_template)
    return http.HttpResponse(outline_template.render())
 
def edit(request):
    outline_template = templates.Outline()
    edit_template = templates.Edit()
    edit_template.set_name('Joe')
    outline_template.set_body(edit_template)
    return http.HttpResponse(outline_template.render())
 
def index_template(request):
    index_template = templates.Index()
    return http.HttpResponse(index_template.load_template())
 
def edit_template(request):
    edit_template = templates.Edit()
    return http.HttpResponse(edit_template.load_template())