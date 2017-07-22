angular.module('b')
    .factory('Level', function ($resource) {
        return $resource('/api/level/:id', {id:'@id'});
    });