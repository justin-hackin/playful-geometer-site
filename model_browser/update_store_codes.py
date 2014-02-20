import os
import csv

from model_browser.models import TextureImplementation

def titlize(afilename):
    return afilename.replace("_", " ").title()

def update_model(model, dicti):
    pass
#     for key, val in dicti.iteritems():
#         model.__dict__[key]=val
#     model.save()

def filter_dictionary(dicti,keys):
    return { k: dicti[k] for k in keys }

def intoDictionary(file):
    reader = csv.reader(open('copy-john.csv'), delimiter=',', quotechar='"')
  


printoutArr = []
def update():    
    craftProductReader = csv.reader(open('model_browser/craft_products.csv'), delimiter=';')
   
    for row in craftProductReader:
        try:
            
            polyhedronName = row[2].replace("3D Models/Craft Kits/", "")
            thisTI = TextureImplementation.objects.get(polyhedron_mapped_to__name= polyhedronName, texture_mapped_from__name=row[1] )
<<<<<<< HEAD
            "Updating craftkit:" + polyhedronName + ":"+row[1]+"|"+row[0]
=======
            print "Updating craftkit:" + polyhedronName + ":"+row[1]+"|"+row[0]
>>>>>>> wonked
            thisTI.craftkit_id = row[0]
            thisTI.save()
        except TextureImplementation.DoesNotExist:
            print "Failed to find craftkit:" + polyhedronName + ":"+row[1]+"|"
    
    lanternProductReader = csv.reader(open('model_browser/lantern_products.csv'), delimiter=';')
   
<<<<<<< HEAD
    for row in lanternProductReader[1,]:
        try:
            polyhedronName = row[2].replace("3D Models/Illuminated Sculptures/", "")
            thisTI = TextureImplementation.objects.get(polyhedron_mapped_to__name= polyhedronName, texture_mapped_from__name=row[1] )
            "Updating lantern:" + polyhedronName + ":"+row[1]+"|"+row[0]
=======
    for row in lanternProductReader:
        try:
            polyhedronName = row[2].replace("3D Models/Illuminated Sculptures/", "")
            thisTI = TextureImplementation.objects.get(polyhedron_mapped_to__name= polyhedronName, texture_mapped_from__name=row[1] )
            print "Updating lantern:" + polyhedronName + ":"+row[1]+"|"+row[0]
>>>>>>> wonked
            thisTI.lantern_id = row[0]
            thisTI.save()
        except TextureImplementation.DoesNotExist:
            print "Failed to find lantern:" + polyhedronName + ":"+row[1]+"|"
            
   
    
    