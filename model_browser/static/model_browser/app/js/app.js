'use strict';

var app = angular.module('pgApp', []);

app.config(function ($routeProvider) {
  $routeProvider
    .when('/home',
      {
        templateUrl: 'static/model_browser/app/partials/home.html'
      })
    .when('/texture-implementations',
      {
        controller: 'TextureImplementationListController',
        templateUrl: 'static/model_browser/app/partials/texture_implementations.html'
      })
    .when('/polyhedrons',
      {
        controller: 'PolyhedronListController',
        templateUrl: 'static/model_browser/app/partials/polyhedrons.html'
      })
      .when('/texture-lines',
      {
        controller: 'TextureLineListController',
        templateUrl: 'static/model_browser/app/partials/texture_lines.html'
      })
    .when('/about',
      {
        templateUrl: 'static/model_browser/app/partials/about.html'
      })
    .otherwise({ redirectTo: '/home' });
});

app.filter('encodeURIComponent', function() {
    return window.encodeURIComponent;
});

app.directive('colorbox', function() {
  return {   
    restrict: 'AC',    
    link: function (scope, element, attrs) {        
      $(element).colorbox(attrs.colorbox);     
    }
  };  
});