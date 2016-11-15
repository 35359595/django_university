(function(){
    'use strict';

    angular.module('univer.frontend', [])
        .controller('UniverController', [ '$scope', '$http', UniverController]);

    function UniverController($scope, $http) {
        $scope.add = function (student, title) {
        var student = {
                title: title
            };
            list.students.push(student);
        };
        $scope.data = [];
        $http.get('/univer/students').then(function(responce){
            $scope.data = responce.data;
        });
    }
})();