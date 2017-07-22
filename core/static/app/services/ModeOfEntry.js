angular.module('b')
    .factory('ModeOfEntry', function ($resource) {
        return $resource('/api/mode-of-entry/:id',{id:'@id'})
    });