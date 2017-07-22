angular.module('b')
    .factory('Courses', function ($resource) {
        return $resource('/api/courses/:id',{id:'@id'});
    });