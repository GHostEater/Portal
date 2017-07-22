angular.module('b').run(runBlock);
  function runBlock(CurrentUser) {
      CurrentUser.setUser();
  }
