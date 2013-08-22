from django.contrib import admin
from model_browser.models import PolyhedronProduct, Polyhedron,\
PolyhedronProductMapping,TextureLine, Texture, TextureImplementation
admin.site.register(PolyhedronProduct)
admin.site.register(Polyhedron)
admin.site.register(PolyhedronProductMapping)
admin.site.register(TextureLine)
admin.site.register(Texture)
admin.site.register(TextureImplementation)

# 
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
# 
# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question']
#     date_hierarchy = 'pub_date'
# 
# 
# 
# 
# admin.site.register(Poll, PollAdmin)