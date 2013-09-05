from rest_framework import serializers
from model_browser.models import TextureImplementation, Polyhedron, Texture, TextureLine


class TextureLineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TextureLine
        fields = ('name', 'description')


class PolyhedronSerializer(serializers.ModelSerializer):
    url_preview_image_small= serializers.CharField()
    url_preview_image_large= serializers.CharField()
    
    class Meta:
        model = Polyhedron
        fields = ('name', 'description', 'url_preview_image_small', 'url_preview_image_large')


class TextureImplementationSerializer(serializers.ModelSerializer):
    polyhedron = serializers.Field(source='polyhedron_mapped_to.name')
    polyhedron_slug = serializers.Field(source='polyhedron_mapped_to.slug')
    texture = serializers.Field(source='texture_mapped_from.name')
    texture_slug = serializers.Field(source='texture_mapped_from.slug')
    texture_line = serializers.Field(source='texture_mapped_from.texture_line.name')
    
    class Meta:
        model = TextureImplementation
        fields = ('polyhedron', 'polyhedron_slug', 'texture', 'texture_slug','texture_line', 'preview_small', 'preview_large')




        



        
