'use strict';
var thisAPI ='http://127.0.0.1:8000/api/';
app.factory('DataFetcher', function($http) {
  
  return {
        
    ti_in_polyhedron_tline: function(polyhedron_slug, texture_line_slug, callback){
    	
    	var thisURL = thisAPI+'texture_implementations/?format=json';
    	if (typeof polyhedron_slug != 'undefined' && typeof texture_line_slug != 'undefined'){
    		thisURL+= '&polyhedron_slug='+polyhedron_slug+'&texture_line_slug='+texture_line_slug;  	}
    	
    	return $http.get(thisURL).success(callback);
    },
    
    ti_in_texture: function(texture_slug, callback){
    	
    	var thisURL = thisAPI+'texture_implementations/?format=json';
    	if (typeof texture_slug != 'undefined'){
    		thisURL+= '&texture_slug='+texture_slug ;}
    	
    	return $http.get(thisURL).success(callback);
    },
    
    polyhedrons_in_texture_line: function(texture_line_slug, callback){
    	var thisURL = thisAPI+'polyhedrons/?format=json';
    	if (typeof texture_line_slug != 'undefined') {
    		thisURL+= '&texture_line_slug='+texture_line_slug; }	
    	return $http.get(thisURL).success(callback);
    },
    
    texture_lines_for_polyhedron: function(polyhedron_slug,  callback){
    	var thisURL = thisAPI+'texture_lines/?format=json';
    	if (typeof polyhedron_slug != 'undefined') {
    		thisURL+='&polyhedron_slug='+polyhedron_slug; }	
    	return $http.get(thisURL).success(callback);
    },
        
  };
});
