# Create your views here.
from django.views import generic
from model_browser import populate_database, queries
from django.template import response
from django.http.response import HttpResponse


class IndexView(generic.TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class ByLineTextureLinesView(IndexView):
    template_name = 'byline_texture_lines.html'
    def get_context_data(self, **kwargs):
        context = super(ByLineTextureLinesView, self).get_context_data(**kwargs)
        context['texture_lines_list'] = queries.all_texture_lines()
        return context
    
class ByLinePolyhedronsView(IndexView):
    template_name = "byline_polyhedrons.html"
  
    def get_context_data(self, **kwargs):
        context = super(ByLinePolyhedronsView, self).get_context_data(**kwargs)
        context['polyhedrons'] = queries.polyhedrons_in_texture_line(self.kwargs['texture_line_id'])
        return context
  
    
#################################

class ByModelPolyhedronsView(IndexView):
    template_name = "bymodel_polyhedrons.html"
  
    def get_context_data(self, **kwargs):
        context = super(ByModelPolyhedronsView, self).get_context_data(**kwargs)
        
        context['polyhedrons'] = queries.all_polyhedrons()
        return context

class ByModelTextureLinesView(IndexView):
    template_name = 'bymodel_texture_lines.html'
    def get_context_data(self, **kwargs):
        context = super(ByModelTextureLinesView, self).get_context_data(**kwargs)
        context['polyhedron_id'] = self.kwargs['polyhedron_id']
        context['texture_lines_list'] = queries.texture_lines_for_polyhedron(context['polyhedron_id'])
        return context
    
#####################
class TextureImplementationView(IndexView):
    template_name = "texture_implementations.html"
    
    def get_context_data(self, **kwargs):
        context = super(TextureImplementationView, self).get_context_data(**kwargs)
        context['texture_implementation_list'] = queries.texture_implementation(self.kwargs['texture_line_id'], self.kwargs['polyhedron_id'])
        return context
    
def populate_db(request):
    return HttpResponse(populate_database.populate())

      