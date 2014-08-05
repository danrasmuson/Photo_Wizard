angular.module('app')
    .controller('ErrorController', function($scope) {
        $scope.errors = [];
        $scope.addError = function(message){
            $scope.errors.push(message);
        }
        $scope.$on('error', function(event, message) {
            $scope.addError(message)
        });
    });