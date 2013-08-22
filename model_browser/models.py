"""
model_browser : represents The Playful Geometer's product line
"""

from django.db import models

# Create your models here.
max_name_length = 30
max_description_length = 500
max_filename_length = 200

"""
ISSUE: id will be automatically derived from name text by .replace(" ","-").lower() 
in populate_database.py
The two names "Cheshire's Cat" and "Cheshire''s Cat" would create same key
Shouldn't be allowed anyway but be careful to catch this anywhere new entries are created

ATTENTION: A "Polyhedron" will be known to the end-user as a "3D Model", this term used to avoid 
    naming confusion and namespace conflicts
although ByModel prefix implies "By Polyhedron" as top level categorization    
"""

class Deactivatable(models.Model):
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract=True
        

class PolyhedronProduct(Deactivatable):
    """
    A product that manifests a given Polyhedron-TextureImplementation mapping.
    Currently, The Playful Geometer carries the "Illumined Stellations" as backlight polyester lanterns and 
    "3D Model Building Kits" as cardstock craftkits, and premade "Ornamental Miniatures"
    """
    id = models.CharField(max_length=max_name_length, primary_key=True)
    name = models.CharField(max_length=max_name_length, unique=True)
    description = models.CharField(max_length=max_description_length, blank=True)    
    
    def __unicode__(self):
        return self.name


class TextureLine(Deactivatable):
    """
    A particular style of Textures that cater to a specific target market i.e. photographic, fractal
    """
    id = models.CharField(max_length=max_name_length, primary_key=True)
    name = models.CharField(max_length=max_name_length, unique=True)
    description = models.CharField(max_length=max_description_length, default="")
        
    def __unicode__(self):
        return self.name
    def hasModels(self, polyhedron_id):
        Polyhedron.objects.filter(id=polyhedron_id, textures__texture_line__id=self.id).distinct()
       
    
class Texture(Deactivatable):
    """
    The design used for decorating a Polyhedron.  A Texture refers to an image while 
    the TextureImplementation refers to a mapping of the image onto a Polyhedron
    """
    id = models.CharField(max_length=max_name_length, primary_key=True)
    name = models.CharField(max_length=max_name_length, unique=True)
    description = models.CharField(max_length=max_description_length, default="")
    texture_line = models.ForeignKey(TextureLine)    
    image_link = models.CharField(max_length=max_filename_length, blank=True)
      
    def __unicode__(self):
        return self.name
    

class Polyhedron(Deactivatable):
    """
    Refered to on the front-end as a "Model", a Polyhedron is a particular 3D shape for which 
    The Playful Geometer sells many varieties featuring different Textures and PolyhedronProducts
    """
    id = models.CharField(max_length=max_name_length, primary_key=True)
    name = models.CharField(max_length=max_name_length, unique=True)
    description = models.CharField(max_length=max_description_length, blank=True)
    points = models.IntegerField(default=0) 
    products = models.ManyToManyField(PolyhedronProduct, through='PolyhedronProductMapping')
    textures = models.ManyToManyField(Texture, through='TextureImplementation')  
        
    def __unicode__(self):
        return self.name
    
    def urlName(self):
        return self.name.replace(' ', '_')
    
    def get_preview_image_small(self):
        return str(self.name).replace(" ","_").lower() + "_blank.min.png"
    
    def get_preview_image_large(self):
        return str(self.name).replace(" ","_").lower()+"_blank.png"
    
    def has_texture_lines(self):
        return TextureLine.objects.filter(texture__textureimplementation__polyhedron_mapped_to=self.id).distinct()

class PolyhedronProductMapping(Deactivatable):
    """
    Defines relationship of Polyhedron shapes to their implementation as PolyhedronProducts
    """
    product = models.ForeignKey(PolyhedronProduct)
    polyhedron = models.ForeignKey(Polyhedron)
    price = models.FloatField()



class TextureImplementation(models.Model):
    """
    A cropped Texture to be mapped onto a particular Polyhedron
    Represents image that can be used as a texture for UV mapping the Polyhedron
    Enables viewing other Polyhedrons with the same Texture 
    """
    texture_mapped_from = models.ForeignKey(Texture)
    polyhedron_mapped_to = models.ForeignKey(Polyhedron)
    preview_small = models.CharField(max_length=max_filename_length)
    preview_large = models.CharField(max_length=max_filename_length)
    
    #textureImplementationFile = models.CharField(max_length=max_filename_length)
    #in future, a webgl texture implementation mapper would use/need
    #    * reference to an ClipPath containing:
    #      * a vector of the polygon (first two points correspond to bottom of texture)
    #      * its rotation center relative to first vertex *fixed*
    #    * position, scale and rotation of ClipPath
     

    
    
    
    

    
    
