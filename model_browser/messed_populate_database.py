import os

from model_browser.models import PolyhedronProduct, Polyhedron, PolyhedronProductMapping, Texture, TextureLine, TextureImplementation

def titlize(afilename):
    return afilename.replace("_", " ").title()

def update_model(model, dicti):
    pass
#     for key, val in dicti.iteritems():
#         model.__dict__[key]=val
#     model.save()

def filter_dictionary(dicti,keys):
    return { k: dicti[k] for k in keys }

    

printoutArr = []
def populate():    
    
    def printout(aStr):
        print aStr
    
    #overwriteExisting = False
    printout("Populating database:")
    
    polyhedrons_dir = "/home/cosmo/Django/playful_geometer_site/model_browser/static/model_browser/images/textured_polyhedrons/"
        
    #column headdings
    
    polyhedron_list = os.listdir(polyhedrons_dir)
    printout(polyhedron_list)
    polyhedron_list = [i for i in polyhedron_list if os.path.isdir(polyhedrons_dir + i)  ] #excludes non-directory entries
    
    #access each model folder
    for polyhedron_name in polyhedron_list:
        printout( "polyhedron_name: " + polyhedron_name)
        polyhedron_folder = polyhedrons_dir + polyhedron_name + "/"
        line_args = {"name":polyhedron_name}
        filter_keys=["name"]
        try:
            this_polyhedron = Polyhedron.objects.get(**filter_dictionary(line_args, filter_keys))
            update_model(this_polyhedron, line_args)
            printout("Updated polyhedron:" + polyhedron_name)
        except Polyhedron.DoesNotExist:
            this_polyhedron = Polyhedron.objects.create( name=polyhedron_name)
            this_polyhedron.save()
            printout(">>>>>Created polyhedron:" + polyhedron_name)
            
        lines_list = os.listdir(polyhedron_folder)
        lines_list = [i for i in lines_list if os.path.isdir(polyhedron_folder + i) ] #excludes non-directory entries or folders starting with 0
        
        for line_name in lines_list:
            printout(">>>Line: " + line_name )
            line_args = {"name":line_name}
            filter_keys=["name"]
            
            try:
                this_line = TextureLine.objects.get(**filter_dictionary(line_args, filter_keys))
                update_model(this_line, line_args)  #may add other args later making this necessary
                printout("Updated line:" + line_name)
            except TextureLine.DoesNotExist:
                this_line = TextureLine.objects.create(**line_args)
                this_line.save()
                printout(">>>>>Created line:"+line_name)
            
            line_folder = polyhedron_folder + line_name + "/"
            
            designs_list = os.listdir(line_folder)
            
            designs_list= [i for i in designs_list if not i.endswith(".min.png") and i.endswith(".png") ] 
            
            for file_ind in range(0, len(designs_list)):
                large_image_name = designs_list[file_ind]
                file_root_name = large_image_name[:-4]
                small_image_name = file_root_name+".min.png"
                if not os.path.exists(line_folder+small_image_name):
                    printout(">>>>>>>>>>>>>>>>>>>>>>>WARNING:Thumbnail does not exist for "+large_image_name)
                polyhedron_design_tup = file_root_name.partition('-')
                design_name = titlize(polyhedron_design_tup[2])
                
                
                texture_args = {'name':design_name, 'texture_line':this_line } 
                filter_keys=["name"]
                try:
                    this_texture = Texture.objects.get(name=design_name)
                    update_model(this_texture, texture_args)
                    printout("Updated texture:" + design_name )
                except Texture.DoesNotExist:
                    this_texture = Texture.objects.create(**texture_args)
                    this_texture.save()
                    printout(">>>>>Created texture:" + design_name)
                
                
                ti_args = {"polyhedron_mapped_to":this_polyhedron, \
                    "texture_mapped_from":this_texture,\
                    "preview_small" :small_image_name, "preview_large" : large_image_name}
                filter_keys = ["polyhedron_mapped_to","texture_mapped_from"]
                try:
                    this_texture_implementation = TextureImplementation.objects.get(**filter_dictionary(ti_args, filter_keys))
                    update_model(this_texture_implementation, ti_args)
                    printout("Updated texture implementation:" + polyhedron_name + "->" + design_name )
                except TextureImplementation.DoesNotExist:
                    this_texture_implementation = TextureImplementation.objects.create(**ti_args)
                    this_texture_implementation.save()
                    printout(">>>>>Created texture implementation:" + polyhedron_name + "->" + design_name)
   
    prices = {"3D Model Building Kits":\
    {'Star Tetrahedron': 12, 'Small Stellated Dodecahedron':20 ,'Great Rhombihexacron':20,'Great Stellated Dodecahedron':25,'Earth Grid Dome':30},\
    "Illumined Stellations":
    {'Star Tetrahedron': 45, 'Small Stellated Dodecahedron':60 ,'Great Rhombihexacron':55,'Great Stellated Dodecahedron':65,'Earth Grid Dome':95} \
    }            
     
    for polyProd, modelPriceRel in prices.iteritems():
        prod_args = {"name":polyProd}
        filter_keys= ["name"]
        try :
            this_polyhedron_product = PolyhedronProduct.objects.get(**filter_dictionary(prod_args, filter_keys))
            update_model(this_polyhedron_product, prod_args)
            printout("Updated product: " + polyProd )

        except PolyhedronProduct.DoesNotExist:
            this_polyhedron_product = PolyhedronProduct.objects.create(**prod_args)
            this_polyhedron_product.save()
            
        for modelName, modelPrice in modelPriceRel.iteritems():
            
            
            try:
                this_polyhedron = Polyhedron.objects.get(name=modelName)
                prod_rel_args={"product":this_polyhedron_product, \
                        "polyhedron":this_polyhedron,\
                        "price":modelPrice}
                filter_keys = ["product", "polyhedron"] 
                try:
                    thisPolyhedronProductMapping = PolyhedronProductMapping.objects.get(**filter_dictionary(prod_rel_args, filter_keys))
                    update_model(thisPolyhedronProductMapping, prod_rel_args)
                    printout(">>>>>Updated product : " + polyProd+ "'s relation to " + modelName)   
                    
                except PolyhedronProductMapping.DoesNotExist:
                    thisPolyhedronProductMapping = PolyhedronProductMapping.objects.create(**prod_rel_args)
                    thisPolyhedronProductMapping.save()
                    printout(">>>>>Created product : " + polyProd+ "'s relation to " + modelName)
                
            except Polyhedron.DoesNotExist:
                printout("Couldn't find Polyhedron: "+ modelName + "for product line: " + polyProd)
    return "\n".join(printoutArr)



if __name__ == "__main__":
    populate()
