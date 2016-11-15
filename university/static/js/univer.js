(function(){
    'use strict';

    angular.module('univer.frontend', ['ngRoute'])
        .controller('UniverController', [ '$scope', '$http', '$location', UniverController]);

    function UniverController($scope, $http, $location) {
        $scope.add = function(lector, s_name, s_las_name, s_email, s_phone){
            if (!!s_name & !!s_las_name & !!s_email & !!s_phone){
            var student = {
                s_lector: lector.id,
                s_name: s_name,
                s_las_name: s_las_name,
                s_email: s_email,
                s_phone: s_phone,
                s_university: lector.l_university,
                s_cathedra: lector.l_cathedra,
                s_disciplins: 1,
                s_ht: 1
            };

            $http.post('/univer/student/', student)
                .then(function(responce){
                       lector.students.push(responce.data);
                    },
                    function(){
                        alert('Could not add new student!');
                    }
                );
            }
        };

        $scope.logout = function(){

        };

        $scope.data = [];
        $scope.GetLectors = function(){
            $http.get('/univer/lector/')
            .then(function(responce){
                $scope.data = responce.data;
            },
            function(){
                alert('403 - Access denied! Login first.');
            }
            );
        }

        $scope.students = [];
        $scope.GetStudents = function(){
            $http.get('/univer/student/')
            .then(function(responce){
                $scope.students = responce.data;
            },
            function(){
                alert('403 - Access denied! Login first.');
            }
            );
        }
    }

    function StudentController(){
        
    }
})();