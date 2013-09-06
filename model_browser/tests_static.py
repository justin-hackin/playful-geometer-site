"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import os
import unittest  # @UnresolvedImport
from django.template.defaultfilters import slugify


def titlize(afilename):
    return afilename.replace("_", " ").title()


def create_model_browser_dict():
    polyhedrons_dir = "/home/cosmo/Django/playful_geometer_site/model_browser/static/model_browser/images/textured_polyhedrons/"
    polyhedron_list = os.listdir(polyhedrons_dir)
    polyhedron_list = [i for i in polyhedron_list if os.path.isdir(polyhedrons_dir + i)   ] #excludes non-directory entries
    model_browser_dict = {i:{} for i in polyhedron_list}
    
    #access each model folder
    for polyhedron_name in polyhedron_list:
        polyhedron_folder = polyhedrons_dir + polyhedron_name + "/"
                     
        lines_list = os.listdir(polyhedron_folder)
        lines_list = [i for i in lines_list if os.path.isdir(polyhedron_folder + i) ] #excludes non-directory entries or folders starting with 0
        model_browser_dict[polyhedron_name] = {i:[] for i in lines_list}
  
        for line_name in lines_list:

            line_folder = polyhedron_folder + line_name + "/"
                
            designs_list = os.listdir(line_folder)
            
            designs_list= [i for i in designs_list if not i.endswith(".min.png") and i.endswith(".png") ] 
            
            for file_ind in range(0, len(designs_list)):
                large_image_name = designs_list[file_ind]
                file_root_name = large_image_name[:-4]
                polyhedron_design_tup = file_root_name.partition('-')
                design_name = titlize(polyhedron_design_tup[2])
                model_browser_dict[polyhedron_name][line_name].append(design_name)
    return model_browser_dict

                
                
polyhedrons_dir = "/home/cosmo/Django/playful_geometer_site/model_browser/static/model_browser/images/textured_polyhedrons/"

class FileSystemTextureCoherence(unittest.TestCase):
    def test_lines_for_all_polyhedrons(self):
        test_msg_array = []
        test_pass = True
        model_browser_dict = create_model_browser_dict()
        for polyhedron_name, polyhedron_lines_dict in model_browser_dict.iteritems():
            for line_name in polyhedron_lines_dict.keys():
                #ensure that every polyhedron has a line of this name
                for test_poly in model_browser_dict.keys():
                    if test_poly != polyhedron_name:
                        
                        line_in_other_poly = polyhedrons_dir + test_poly + "/"+line_name
                        
                        if not os.path.exists(line_in_other_poly):
                            test_pass = False
                            test_msg_array.append("%s from %s not in %s"%(polyhedron_name, line_name, test_poly) )
                        if slugify(line_name) == slugify(line_in_other_poly):
                            test_pass = False
                            test_msg_array.append("Slug for %s in %s is the same as for %s in %s (but don't worry, SlugField will make it unique ;)" % (polyhedron_name, line_name, test_poly, line_in_other_poly) )
                            
        test_msg_array.append("\n\n NOTE: although this this is not a critical fail,\
         it might suggest some incongruency with Texture Line names across models \
         Slug errors won't break site because SlugField ensures slugs will be unique \
         If you have them though, TextureImplementations may not be linked through Textures \
         because there will be 2 slightly different   ")
        
        self.assertEqual(test_pass, True, "\n".join(test_msg_array))

                
    def test_line_design_conflict(self):
        """
        Avoid the following: Texture "Games Begin" has TextureImplementation in multiple lines according
         to the file structure but it can only belong to one line according to the database
         i.e. ...    textured_polyhedrons/Great Stellated Dodecahedron/Cosmic SpaceCrafts Vol.1/great_stellated_dodecahedron-games_begin.png
                     textured_polyhedrons/Great Stellated Dodecahedron/Cosmic SpaceCrafts Vol.2/small_stellated_dodecahedron-games_begin.png
         
         """
        test_msg_array = []
        test_pass = True
        model_browser_dict = create_model_browser_dict()
        print model_browser_dict
        #for every polyhedron ..
        for polyhedron_name, polyhedron_lines_dict in model_browser_dict.iteritems():
            #and every texture line within that polyhedron
            for line_name, designs_list in polyhedron_lines_dict.iteritems():
                #look at every other polyhedron
                for other_polyhedron_name, other_polyhedron_lines_dict in model_browser_dict.iteritems():
                    #(only check in a different polyhedron)
                    if other_polyhedron_name != polyhedron_name:
                        #and every line within that polyhedron
                        for other_line_name, other_designs_list in other_polyhedron_lines_dict.iteritems():
                            #(only check in a different texture line)
                            if other_line_name != line_name:
                                #check to see if there is the same texture in a different texture line for a different model
                                for other_design in other_designs_list:
                                    if other_design in designs_list:
                                        test_pass = False
                                        test_msg_array.append(":".join([polyhedron_name, line_name, other_design])+"\nCONFLICTS WITH\n"+":".join([other_polyhedron_name, other_line_name])+"\nSAME TEXTURE IN DIFFERENT LINES\n")
        
                                
        self.assertEqual(test_pass, True, "\n".join(test_msg_array))
                
if __name__ == "__main__":
    unittest.main()                     
                 
                 
                 
                 
