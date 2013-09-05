'use strict';

var app = angular.module('pgApp', []);

app.config(function ($routeProvider) {
  $routeProvider
    .when('/home',
      {
        templateUrl: 'static/model_browser/app/partials/home.html'
      })
    .when('/models',
      {
        controller: 'TextureImplementationListController',
        templateUrl: 'static/model_browser/app/partials/models.html'
      })
    .when('/model/:polyhedronSlug/:textureSlug',
      {
        controller: 'TextureImplementationDetailController',
        templateUrl: 'static/model_browser/app/partials/model.html'
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
