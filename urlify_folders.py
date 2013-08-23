import os

def titlize(afilename):
    return afilename.replace("_", " ").title()

def urlize(name):
    return name.replace(" ", "_")


#overwriteExisting = False
print "Populating database:"
polyhedrons_dir = "/home/cosmo/Django/playful_geometer_site/model_browser/static/model_browser/images/textured_polyhedrons/"
    
#column headdings

polyhedron_list = os.listdir(polyhedrons_dir)
print polyhedron_list
polyhedron_list = [i for i in polyhedron_list if os.path.isdir(polyhedrons_dir + i)  ] #excludes non-directory entries

#access each model folder
for polyhedron_name in polyhedron_list:
    print "polyhedron_name: " + polyhedron_name
    polyhedron_url = urlize(polyhedron_name) 
    polyhedron_folder_old = polyhedrons_dir + polyhedron_name + "/"
    polyhedron_folder = polyhedrons_dir + polyhedron_url + "/"

    os.rename(polyhedron_folder_old, polyhedron_folder)               
    lines_list = os.listdir(polyhedron_folder)
    lines_list = [i for i in lines_list if os.path.isdir(polyhedron_folder + i) and not i.startswith("0")] #excludes non-directory entries or folders starting with 0
    
    for line_name in lines_list:
        print ">>>Line: " + line_name 
        line_key = urlize(line_name)
        line_folder_old = polyhedron_folder + line_name + "/"
        line_folder = polyhedron_folder + line_key + "/"
        os.rename(line_folder_old, line_folder)
