angular.module('b')
    .factory('Lecturer', function ($resource) {
        return $resource('/api/lecturer/:id',{id:'@id'});
    });