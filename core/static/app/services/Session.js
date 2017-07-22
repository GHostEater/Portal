angular.module('b')
    .factory('Session', function ($resource) {
        return $resource('/api/session/:id', {id:'@_id'},{
            getCurrent:{
                method: 'get',
                url: '/api/session-current/1/'
            }
        });
    });