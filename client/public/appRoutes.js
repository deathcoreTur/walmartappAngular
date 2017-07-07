'use strict';

angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider ) {

        $stateProvider.state({
            name: 'products',
            url: '/',
            templateUrl: 'public/components/products/templates/products.template.html',
            controller: 'ProductsController'
        });

        $urlRouterProvider.otherwise('/');
    }]);