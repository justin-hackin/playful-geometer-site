# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from model_browser.models import TextureImplementation, TextureLine, Polyhedron
from model_browser.serializers import TextureImplementationSerializer, TextureLineSerializer,\
    PolyhedronSerializer
from django.views.generic import TemplateView
import queries


class Gallery3d(TemplateView):
   template_name = "model_browser/3d_view.html"

def models_gallery(request):
    context = {}
    return render(request, 'model_browser/index.html', context)

class TextureImplementationViewSet(viewsets.ModelViewSet):
    serializer_class = TextureImplementationSerializer
    queryset = queries.all_texture_implementations() 
       
    def get_queryset(self):
        
        polyhedron_slug = self.request.QUERY_PARAMS.get('polyhedron_slug', None)
        texture_line_slug = self.request.QUERY_PARAMS.get('texture_line_slug', None)
        texture_slug =  self.request.QUERY_PARAMS.get('texture_slug', None)
                
        if polyhedron_slug!=None  and texture_line_slug!=None:
            return queries.texture_implementations(texture_line_slug, polyhedron_slug)
        elif texture_slug == None and polyhedron_slug == None :
            return queries.all_texture_implementations()
        elif texture_slug != None:
            return queries.texture_implementations_in_texture(texture_slug)
        elif polyhedron_slug != None:
            return queries.texture_implementations_for_polyhedron(polyhedron_slug)
        



class TextureLineViewSet(viewsets.ModelViewSet):
    serializer_class = TextureLineSerializer
    queryset = queries.all_texture_lines()
    
    def get_queryset(self):
        polyhedron_slug = self.request.QUERY_PARAMS.get('polyhedron_slug', None)
        if polyhedron_slug:
            return queries.texture_lines_for_polyhedron(polyhedron_slug)
        else:
            return self.queryset

class PolyhedronViewSet(viewsets.ModelViewSet):
    serializer_class = PolyhedronSerializer
    queryset = queries.all_polyhedrons()
    def get_queryset(self):
        texture_line_slug = self.request.QUERY_PARAMS.get('texture_line_slug', None)
        
        if texture_line_slug:
            return queries.polyhedrons_in_texture_line(texture_line_slug)
        else :
            return self.queryset
        

