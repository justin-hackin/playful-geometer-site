import os

from model_browser.models import PolyhedronProduct, Polyhedron, PolyhedronProductMapping, Texture, TextureLine, TextureImplementation

def titlize(afilename):
    return afilename.replace("_", " ").title()

def urlize(name):
    return name.replace(" ", "_")

def unurlize(name):
    return name.replace("_", " ")
#TODO:  throw exception if name attributes contain special characters 

def populateDatabase():    
    #overwriteExisting = False
    print "Populating database:"
    polyhedrons_dir = "/home/cosmo/Django/playful_geometer_site/model_browser/static/model_browser/images/textured_polyhedra/"
        
    #column headdings
    
    polyhedron_list = os.listdir(polyhedrons_dir)
    print polyhedron_list
    polyhedron_list = [i for i in polyhedron_list if os.path.isdir(polyhedrons_dir + i)  ] #excludes non-directory entries
    
    #access each model folder
    for polyhedron_url in polyhedron_list:
        polyhedron_name = unurlize(polyhedron_url)
        print "polyhedron_name: " + polyhedron_name
        polyhedron_folder = polyhedrons_dir + polyhedron_url + "/"
        try:
            this_polyhedron = Polyhedron.objects.get(name=polyhedron_name)
            print "Found polyhedron:" + polyhedron_name
        except Polyhedron.DoesNotExist:
            this_polyhedron = Polyhedron.objects.create(name=polyhedron_name, id=polyhedron_url)
            this_polyhedron.save()
            print ">>>>>Created polyhedron:" + polyhedron_name
            
            
               
        lines_list = os.listdir(polyhedron_folder)
        lines_list = [i for i in lines_list if os.path.isdir(polyhedron_folder + i) and not i.startswith("0")] #excludes non-directory entries or folders starting with 0
        
        for line_url in lines_list:
            line_name = unurlize(line_url)
            print ">>>Line: " + line_name 
            try:
                this_line = TextureLine.objects.get(name=line_name)
                print "Found line:" + line_name
            except TextureLine.DoesNotExist:
                this_line = TextureLine.objects.create(name=line_name, id=line_url)
                this_line.save()
                print ">>>>>Created line:"+line_name
            
            relative_model_previews_path=  "/"+"/".join([polyhedron_url, line_url])+"/"
            line_folder = polyhedron_folder + line_url + "/"
            
            designs_list = os.listdir(line_folder)
            designs_list.sort() #so large and small images are together in array
            
            
            for file_ind in range(0, len(designs_list), 2):
                small_image_name = designs_list[file_ind]
                large_image_name = designs_list[file_ind+1]
                file_root_name = large_image_name[:-4]
                polyhedron_design_tup = file_root_name.partition('-')
                #polyhedronTitle = titlize(polyhedron_design_tup[0])
                #polyhedronKey = urlize(polyhedronTitle)
                design_name = titlize(polyhedron_design_tup[2])
                design_key = urlize(design_name)
                  
                try:
                    this_texture = Texture.objects.get(name=design_name)
                    print "Found texture:" + design_name 
                except Texture.DoesNotExist:
                    this_texture = Texture.objects.create(name=design_name, id=design_key, texture_line=this_line)
                    this_texture.save()
                    print ">>>>>Created texture:" + design_name
                
                try:
                    this_texture_implementation = TextureImplementation.objects.get(polyhedron_mapped_to=this_polyhedron, texture_mapped_from=this_texture)
                    print "Found texture implementation:" + polyhedron_name + "->" + design_name 
                except TextureImplementation.DoesNotExist:
                    this_texture_implementation = TextureImplementation.objects.create(\
                    polyhedron_mapped_to=this_polyhedron, \
                    texture_mapped_from=this_texture,\
                    preview_small = relative_model_previews_path+small_image_name,\
                    preview_large = relative_model_previews_path+large_image_name)
                    this_texture_implementation.save()
                    print ">>>>>Created texture implementation:" + polyhedron_name + "->" + design_name
   
    prices = {"3D Model Building Kits":\
    {'Star Tetrahedron': 12, 'Small Stellated Dodecahedron':20 ,'Great Rhombihexacron':20,'Great Stellated Dodecahedron':25,'Earth Grid Dome':30},\
    "Illumined Stellations":
    {'Star Tetrahedron': 45, 'Small Stellated Dodecahedron':60 ,'Great Rhombihexacron':55,'Great Stellated Dodecahedron':65,'Earth Grid Dome':95} \
    }            
     
    for polyProd, modelPriceRel in prices.iteritems():
        try :
            this_polyhedron_product = PolyhedronProduct.objects.get(name=polyProd)
        except PolyhedronProduct.DoesNotExist:
            this_polyhedron_product = PolyhedronProduct(name=polyProd, id=urlize(polyProd))
        for modelName, modelPrice in modelPriceRel.iteritems():
            try:
                this_polyhedron = Polyhedron.objects.get(name=modelName)
                try:
                    PolyhedronProductMapping.objects.get(polyhedron=this_polyhedron, product=this_polyhedron_product)
                except PolyhedronProductMapping.DoesNotExist:
                    thisPolyhedronProductMapping = PolyhedronProductMapping(\
                        product=this_polyhedron_product, \
                        polyhedron=this_polyhedron,\
                        price=modelPrice)
                    thisPolyhedronProductMapping.save()
                print ">>>>>Created product : " + polyProd+ "'s relation to " + modelName
                
            except Polyhedron.DoesNotExist:
                print "Couldn't find Polyhedron: "+ modelName + "for product line: " + polyProd


