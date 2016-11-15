(function(){
    'use strict';
    angular.module('univer.frontend')
        .directive('univerStudent', UniverStudent);

        function UniverStudent(){
            return{
                templateUrl: 'static/html/student.html',
                restrict: 'E',
                controller: ['$scope', '$http', function($scope, $http){
                    var url = '/univer/student/' + $scope.student.id + '/';
                  
                //function for editing the item
                $scope.update = function(){
                    return $http.put(
                        url,
                        $scope.student
                    );
                };

                //move to other list
                $scope.move = function(){
                    if ($scope.destLector === undefined){
                        return;
                    }
                    $scope.student.lector = $scope.destLector.id;
                    $scope.update().then(function(){
                        {
                            removeStudentFromLector($scope.student, $scope.lector);
                            $scope.destLector.students.push($scope.student);
                        }
                    });
                };

                function removeStudentFromLector(student, lector){
                    var students = lector.students;
                    students.splice(
                        students.indexOf(student),
                        1
                    );
                }

                //function for remove of object from DB
                $scope.delete = function() {
                    $http.delete(url).then(
                        //reload list in UI
                        removeStudentFromLector($scope.student, $scope.lector)
                    );
                };

                $scope.modelOptions = {
                    debounce: 1000
                };
                }]
            };
        }
})();