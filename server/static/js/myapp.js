(function () {
    'use strict';

    angular
        .module('myapp', [
            'myapp.config',
            'myapp.routes',
            'myapp.authentication'
        ]);

    angular
        .module('myapp').run(run);

    run.$inject = ['$http'];


    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

    angular
        .module('myapp.routes', ['ngRoute']);
    angular
        .module('myapp.config', []);
})();
