from model_browser.models import TextureLine, Polyhedron, TextureImplementation 

def texture_lines_for_polyhedron(polyhedron_slug):
    return TextureLine.objects.filter(texture__textureimplementation__polyhedron_mapped_to__slug=polyhedron_slug).distinct()

def all_texture_lines():
    return TextureLine.objects.filter(is_active=True)

def all_polyhedrons():
    return Polyhedron.objects.filter(is_active=True)
    
def polyhedrons_in_texture_line(texture_line_slug):
    return Polyhedron.objects.filter(textures__texture_line__slug=texture_line_slug, \
                                     is_active=True).distinct()

def texture_implementations(texture_line_slug, polyhedron_slug):
    """Assumes requested texture_line and polyhedron are active""" 
    return TextureImplementation.objects.filter(\
            texture_mapped_from__texture_line__slug=texture_line_slug, 
            polyhedron_mapped_to__slug=polyhedron_slug, \
            is_active=True)
    
def all_texture_implementations():
    return TextureImplementation.objects.filter(is_active=True)

def texture_implementations_in_texture(texture_slug):
    return TextureImplementation.objects.filter(is_active=True, texture_mapped_from__slug=texture_slug)