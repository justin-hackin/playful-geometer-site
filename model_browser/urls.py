from django.conf.urls import patterns, include, url
from model_browser import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# note bymodel prefix implies "By Polyhedron" as top level categorization
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^$', views.PolyhedronListView.as_view(), name='polyhedron_list_view'),
    url(r'^TextureLines/$', views.ByLineTextureLinesView.as_view(), name='byline_texture_lines_view'),
    url(r'^TextureLines/(?P<texture_line_slug>[-\w]+)/$', views.ByLinePolyhedronsView.as_view(), name="byline_polyhedrons_view"),
    url(r'^TextureLines/(?P<texture_line_slug>[-\w]+)/(?P<polyhedron_slug>[-\w]+)/$', views.TextureImplementationView.as_view(), name='byline_texture_implementation_view'),
    url(r'^Models/$', views.ByModelPolyhedronsView.as_view(), name='bymodel_polyhedrons_view'),
    url(r'^Models/(?P<polyhedron_slug>[-\w]+)/$', views.ByModelTextureLinesView.as_view(), name='bymodel_texture_lines_view'),
    url(r'^Models/(?P<polyhedron_slug>[-\w]+)/(?P<texture_line_slug>[-\w]+)/$', views.TextureImplementationView.as_view(), name='bymodel_texture_implementation_view'),
    url(r'^PopulateDatabase/$', views.populate_db, name='populate_database_view'),
    #url(r'^/Textues/')
    #url(r'/TextureLines/(?P<texture_line_url>\d+)', views.PolyhedronListView, name='texture_lines'),

    # url(r'^playful_geometer_site/', include('playful_geometer_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
