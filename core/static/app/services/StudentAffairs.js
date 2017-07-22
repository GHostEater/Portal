angular.module('b')
    .factory('StudentAffairs', function ($resource) {
        return $resource('/api/student-affairs/:id',{id:'@id'});
    });