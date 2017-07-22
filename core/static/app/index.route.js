angular.module('b').config(routerConfig);

function routerConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('home', {url: '/', templateUrl: '/static/app/home/home.html'})
        .state('studentUpload', {url: '/student-upload/', templateUrl: '/static/app/student/studentUpload.html'})
        .state('courseToMajor', {url: '/course-to-major/', templateUrl: '/static/app/courseToMajor/courseToMajor.html'});

    $urlRouterProvider.otherwise('/');
}
