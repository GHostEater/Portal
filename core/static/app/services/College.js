angular.module('b')
    .factory('College', function ($resource) {
        return $resource('/api/college/:id',{id:'@id'});
    });