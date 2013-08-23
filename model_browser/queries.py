from model_browser.models import TextureLine, Polyhedron, TextureImplementation 

def texture_lines_for_polyhedron(polyhedron_id):
    return TextureLine.objects.filter(texture__textureimplementation__polyhedron_mapped_to=polyhedron_id).distinct()

def all_texture_lines():
    return TextureLine.objects.all()

def all_polyhedrons():
    return Polyhedron.objects.all()
    
def polyhedrons_in_texture_line(texture_line_id):
    return Polyhedron.objects.filter(textures__texture_line__id=texture_line_id).distinct()

def texture_implementation(texture_line_id, polyhedron_id):
    return TextureImplementation.objects.filter(\
            texture_mapped_from__texture_line__id=texture_line_id, polyhedron_mapped_to__id=polyhedron_id)
    
