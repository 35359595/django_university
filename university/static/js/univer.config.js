(function(){
    'use strict';

    angular.module('univer.frontend')
        .config(['$routeProvider', config])
        .run(['$http', run]);

    function config($routeProvider){
        $routeProvider
            .when('/',{
                templateUrl: '/static/html/lectors.html',
                controller: 'UniverController',
            })
            .when('/login',{
                templateUrl: 'static/html/login.html',
                controller: 'LoginController',
            })
            .when('/students', {
                templateUrl: 'static/html/students.html',
            })
            .otherwise('/null');
    }

    function run($http){
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken'; 
    }
})();