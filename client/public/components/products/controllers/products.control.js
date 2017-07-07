products
    .controller('ProductsController', function ($scope, Products) {
        Products.query().$promise.then(function (data) {
            $scope.products = data;
        })
    });