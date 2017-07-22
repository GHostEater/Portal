angular.module('b')
    .factory('Semester', function ($resource) {
        return $resource('/api/semester/:id',{id:'@id'},{
            get:{
                method: 'get',
                url: '/api/semester/1'
            },
            changeSemester:{
                method: 'put'
            }
            });
    });