angular.module('app')
    .controller('ImagesController', function($scope, $http, $rootScope) {
        $scope.images = [];
        $scope.getImage = function(query){
            $http.post('http://127.0.0.1:5000/GetImage', {"query":query})
            .then(function (result) {
                if (result.data === "404"){
                    $rootScope.$broadcast('error', 'No Results For Query: '+query);
                } else{
                    $scope.addImage(result.data);
                }
            });
        }
        $scope.addImage = function(path){
            $scope.images.push(path);
        }
        $scope.getImages = function(){
            var queries = document.getElementById('queries').value.split("\n");
            for (var i = 0; i < queries.length; i++) {
                $scope.getImage(queries[i]);
            }
        }
    });
