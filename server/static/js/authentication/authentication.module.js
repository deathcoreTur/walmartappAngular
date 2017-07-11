(function () {
  'use strict';

  angular
    .module('myapp.authentication', [
      'myapp.authentication.controllers',
      'myapp.authentication.services'
    ]);

  angular
    .module('myapp.authentication.controllers', []);

  angular
    .module('myapp.authentication.services', ['ngCookies']);
})();