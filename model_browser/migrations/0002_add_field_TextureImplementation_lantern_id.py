# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TextureImplementation.lantern_id'
        db.add_column(u'model_browser_textureimplementation', 'lantern_id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=6),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TextureImplementation.lantern_id'
        db.delete_column(u'model_browser_textureimplementation', 'lantern_id')


    models = {
        u'model_browser.polyhedron': {
            'Meta': {'object_name': 'Polyhedron'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['model_browser.PolyhedronProduct']", 'through': u"orm['model_browser.PolyhedronProductMapping']", 'symmetrical': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'textures': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['model_browser.Texture']", 'through': u"orm['model_browser.TextureImplementation']", 'symmetrical': 'False'})
        },
        u'model_browser.polyhedronproduct': {
            'Meta': {'object_name': 'PolyhedronProduct'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'model_browser.polyhedronproductmapping': {
            'Meta': {'object_name': 'PolyhedronProductMapping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'polyhedron': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model_browser.Polyhedron']"}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model_browser.PolyhedronProduct']"})
        },
        u'model_browser.texture': {
            'Meta': {'object_name': 'Texture'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'image_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'texture_line': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model_browser.TextureLine']"})
        },
        u'model_browser.textureimplementation': {
            'Meta': {'object_name': 'TextureImplementation'},
            'craftkit_id': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lantern_id': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'polyhedron_mapped_to': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model_browser.Polyhedron']"}),
            'preview_large': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'preview_small': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'texture_mapped_from': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['model_browser.Texture']"})
        },
        u'model_browser.textureline': {
            'Meta': {'object_name': 'TextureLine'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        }
    }

    complete_apps = ['model_browser']