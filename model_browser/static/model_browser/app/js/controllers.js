'use strict';

app.controller('TextureImplementationListController', function($scope, $location, DataFetcher) {
  var polyhedron_slug = $location.search().polyhedron_slug;
  var texture_line_slug = $location.search().texture_line_slug;
  var texture_slug = $location.search().texture_slug;
  if (typeof texture_slug != 'undefined'){
  	DataFetcher.ti_in_texture(texture_slug, 
	  	function(data) {    
	    $scope.texture_implementation_list = data;
	    $scope.headding = "Texture: "+data[0].texture ;
	  });
  }else{  
	  DataFetcher.ti_in_polyhedron_tline(polyhedron_slug, texture_line_slug, 
	  	function(data) {    
	    $scope.texture_implementation_list = data;
	    $scope.headding = "Model: "+data[0].polyhedron;
	  });
	}
});

app.controller('PolyhedronListController', function($scope, $location, DataFetcher) {
  var texture_line_slug = $location.search().texture_line_slug;
    
  DataFetcher.polyhedrons_in_texture_line(texture_line_slug, 
  	function(data) {    
    $scope.polyhedron_list = data;
    $scope.texture_line_slug = texture_line_slug ;
  });
});

app.controller('TextureLineListController', function($scope, $location, DataFetcher) {
  var polyhedron_slug = $location.search().polyhedron_slug;
    
  DataFetcher.texture_lines_for_polyhedron(polyhedron_slug, 
  	function(data) {    
    $scope.texture_line_list = data;
    $scope.polyhedron_slug = polyhedron_slug;
    
  });
});

app.controller('TextureImplementationDetailController',
    function($scope, $location, DataFetcher) {
    	var polyhedron_slug = $location.search().polyhedron_slug;
  		var texture_slug = $location.search().texture_slug;
    	DataFetcher.ti_details($routeParams.polyhedronSlug, $routeParams.textureSlug, function(data) {
	    $scope.model = data;
	  });
});


app.controller('NavbarController', function($scope, $location) {
  $scope.getActive = function(path) {
    return $location.url().split('?')[0] == path;
  }
});

