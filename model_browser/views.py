# Create your views here.
from django.views import generic
from .models import TextureLine, Polyhedron
from django.shortcuts import render
from model_browser.models import TextureImplementation, Texture
from model_browser import populate_database

class IndexView(generic.TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class ByLineTextureLinesView(IndexView):
    template_name = 'byline_texture_lines.html'
    def get_context_data(self, **kwargs):
        context = super(ByLineTextureLinesView, self).get_context_data(**kwargs)
        context['texture_lines_list'] = TextureLine.objects.all()
        return context
    
class ByLinePolyhedronsView(ByLineTextureLinesView):
    template_name = "byline_polyhedrons.html"
  
    def get_context_data(self, **kwargs):
        context = super(ByLinePolyhedronsView, self).get_context_data(**kwargs)
        context['polyhedrons'] = Polyhedron.objects.filter(textures__texture_line__id=self.kwargs['texture_line_id']).distinct()
        return context
  
class ByLineTextureImplementationView(ByLinePolyhedronsView):
    template_name = "texture_implementations.html"
    
    def get_context_data(self, **kwargs):
        context = super(ByLineTextureImplementationView, self).get_context_data(**kwargs)
        context['texture_implementation_list'] = TextureImplementation.objects.filter(\
            texture_mapped_from__texture_line__id=self.kwargs['texture_line_id'], polyhedron_mapped_to__id=self.kwargs['polyhedron_id'])
        return context
    
    
#################################

class ByModelPolyhedronsView(IndexView):
    template_name = "bymodel_polyhedrons.html"
  
    def get_context_data(self, **kwargs):
        context = super(ByModelPolyhedronsView, self).get_context_data(**kwargs)
        
        context['polyhedrons'] = Polyhedron.objects.all()
        return context

class ByModelTextureLinesView(ByModelPolyhedronsView):
    template_name = 'bymodel_texture_lines.html'
    def get_context_data(self, **kwargs):
        context = super(ByModelTextureLinesView, self).get_context_data(**kwargs)
        context['polyhedron_id'] = self.kwargs['polyhedron_id']
        p = Polyhedron.objects.get(id=context['polyhedron_id'])
        context['texture_lines_list'] = p.has_texture_lines() 
        
        #textures_implementations_on_polyhedron = TextureImplementation.objects.get(model)
        #textures_in_model = Texture.object.
        # what is the reverse of getting the TextureLines that have TextureImplimentations on a given Model
        # a list of models that have TextureImplementations in a given TextureLine
        
        #TODO: only display texture lines that have models that are decorated by a texture from given model line
        return context
  
class ByModelTextureImplementationView(ByModelTextureLinesView):
    template_name = "texture_implementations.html"
    
    def get_context_data(self, **kwargs):
        context = super(ByModelTextureImplementationView, self).get_context_data(**kwargs)
        context['texture_implementation_list'] = TextureImplementation.objects.filter(\
            texture_mapped_from__texture_line__id=self.kwargs['texture_line_id'], polyhedron_mapped_to__id=self.kwargs['polyhedron_id'])
        return context

