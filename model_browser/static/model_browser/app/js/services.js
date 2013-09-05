'use strict';

app.factory('TextureImplementation', function($http) {

  function getUrl(id ) {
    id = (typeof id !== 'undefined') ? id : '';
    return 'http://127.0.0.1:8000/api/models/' + id + '?format=json';
  }

  return {
    get: function(id, callback) {
      return $http.get(getUrl(id)).success(callback);
    },
    query: function(page, page_size, callback) {
      return $http.get(getUrl() + '&page_size=' + page_size + '&page=' + page).success(callback);
    }
    
  };
});
