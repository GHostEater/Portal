angular.module('b')
    .factory('CurrentUser', function ($http,$rootScope) {
        var profile = {};

        function setUser() {
            $http.get('/api/current-user')
                .then(function(response){
                   profile = response.data;
                   $rootScope.user = response.data;
                });
        }
        return {
            setUser: setUser,
            profile: profile
        }
    });