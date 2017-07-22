angular.module('b')
    .factory('CollegeOfficer', function ($resource) {
        return $resource('/api/college-officer/:id',{id:'@id'});
    });