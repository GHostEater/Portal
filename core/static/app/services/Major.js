angular.module('b')
    .factory('Major', function ($resource) {
        return $resource('/api/major/:id',{id:'@id'});
    });