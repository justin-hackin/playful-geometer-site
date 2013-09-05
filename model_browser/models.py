"""
model_browser : represents The Playful Geometer's product line
"""

from django.db import models
from autoslug import AutoSlugField  # @UnresolvedImport 
from django.utils.encoding import filepath_to_uri

# Create your models here.
max_name_length = 50
max_description_length = 500
max_filename_length = 200

"""

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
    name = models.CharField(max_length=max_name_length, primary_key=True)
    slug = AutoSlugField(unique=True, populate_from='name')
    description = models.CharField(max_length=max_description_length, blank=True)    
    
    def __unicode__(self):
        return self.name
    

class TextureLine(Deactivatable):
    """
    A particular style of Textures that cater to a specific target market i.e. photographic, fractal
    """
    name = models.CharField(max_length=max_name_length, primary_key=True)
    slug = AutoSlugField(unique=True, populate_from='name')
    description = models.CharField(max_length=max_description_length, default="")
    
    def __unicode__(self):
        return self.name
    
class Texture(Deactivatable):
    """
    The design used for decorating a Polyhedron.  A Texture refers to an image while 
    the TextureImplementation refers to a mapping of the image onto a Polyhedron
    """
    name = models.CharField(max_length=max_name_length, primary_key=True)
    slug = AutoSlugField(unique=True, populate_from='name')
    description = models.CharField(max_length=max_description_length, default="")
    texture_line = models.ForeignKey(TextureLine)    
    image_link = models.CharField(max_length=max_filename_length, blank=True)
    
    def __unicode__(self):
        return self.name  


white_polyhedrons_url = "model_browser/images/white_polyhedrons/"

class Polyhedron(Deactivatable):
    """
    Refered to on the front-end as a "Model", a Polyhedron is a particular 3D shape for which 
    The Playful Geometer sells many varieties featuring different Textures and PolyhedronProducts
    """
    name = models.CharField(max_length=max_name_length, primary_key=True)
    description = models.CharField(max_length=max_description_length, blank=True)
    slug = AutoSlugField(unique=True, populate_from='name')
    points = models.IntegerField(default=0) 
    products = models.ManyToManyField(PolyhedronProduct, through='PolyhedronProductMapping')
    textures = models.ManyToManyField(Texture, through='TextureImplementation')  
    
    def __unicode__(self):
        return self.name
        
    def url_preview_image_small(self):
        return white_polyhedrons_url+str(self.name).replace(" ","_").lower() + "_blank.min.png"
    
    def url_preview_image_large(self):
        return white_polyhedrons_url+str(self.name).replace(" ","_").lower()+"_blank.png"


class PolyhedronProductMapping(Deactivatable):
    """
    Defines relationship of Polyhedron shapes to their implementation as PolyhedronProducts
    """
    
    product = models.ForeignKey(PolyhedronProduct)
    polyhedron = models.ForeignKey(Polyhedron)
    price = models.FloatField()
    
    def __unicode__(self):
        return self.product.name + "->" + self.polyhedron.name


class TextureImplementation(Deactivatable):
    """
    A cropped Texture to be mapped onto a particular Polyhedron
    Represents image that can be used as a texture for UV mapping the Polyhedron
    Enables viewing other Polyhedrons with the same Texture 
    """
    texture_mapped_from = models.ForeignKey(Texture)
    polyhedron_mapped_to = models.ForeignKey(Polyhedron)
    preview_small = models.CharField(max_length=max_filename_length)
    preview_large = models.CharField(max_length=max_filename_length)
    
    def __unicode__(self):
        return self.texture_mapped_from.name + "->" + self.polyhedron_mapped_to.name 
    
    def get_base_url(self):
        return filepath_to_uri("model_browser/images/textured_polyhedrons/"+self.polyhedron_mapped_to.name +"/"+self.texture_mapped_from.texture_line.name+"/")

    def url_preview_image_small(self):
        return self.get_base_url()+self.preview_small
    
    def url_preview_image_large(self):
        return self.get_base_url()+self.preview_large
    
    
    #textureImplementationFile = models.CharField(max_length=max_filename_length)
    #in future, a webgl texture implementation mapper would use/need
    #    * reference to an ClipPath containing:
    #      * a vector of the polygon (first two points correspond to bottom of texture)
    #      * its rotation center relative to first vertex *fixed*
    #    * position, scale and rotation of ClipPath
     

    
    
    
    

    
    
