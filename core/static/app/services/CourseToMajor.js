angular.module('b')
    .factory('CourseToMajor', function ($resource) {
        return $resource('/api/course-to-major/:id',{id:'@id'});
    });