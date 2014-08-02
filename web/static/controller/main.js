angular.module('app', []);

angular.module('app')
    .controller('PageController', function($scope) {
        $scope.imageTemplate = "views/images.html";
        $scope.errorTemplate = "views/error.html";
    });