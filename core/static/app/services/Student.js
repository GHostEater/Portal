angular.module('b')
    .factory('Student', function ($resource) {
        return $resource('/api/student/:id',{id:'@id'},{
            upload:{
                url: '/api/student/new/',
                method: 'post'
            }
        });
    });