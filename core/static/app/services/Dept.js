angular.module('b')
    .factory('Dept', function ($resource) {
        return $resource('/api/dept/:id',{id:'@id'});
    });