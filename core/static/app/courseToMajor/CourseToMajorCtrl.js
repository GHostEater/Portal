/**
 * Created by GHostEater on 16-Jun-17.
 */
angular.module('b')
    .controller("CourseToMajorCtrl",function (CourseToMajor,College,Dept,Major,Level,toastr,lodash,$uibModal) {
        var vm = this;
        vm.colleges = College.query();
        vm.levels = Level.query();
        vm.d = Dept.query();
        vm.m = Major.query();
        vm.getDepts = getDepts;
        vm.getMajors = getMajors;
        vm.getMajorCourses = getMajorCourses;
        vm.add = add;
        vm.remove = remove;

        function getDepts(college){
            vm.depts = lodash.filter(vm.d,{college:college});
        }
        function getMajors(dept){
            vm.majors = lodash.filter(vm.m,{dept:dept});
        }
        function getMajorCourses(id){
            vm.major = lodash.find(vm.m,{id:Number(id)});
            vm.majorCourses = CourseToMajor.query({majorId:id});
        }
        function add(majorId){
                var options = {
                    templateUrl: '/static/app/courseToMajor/courseToMajorAdd.html',
                    controller: "CourseToMajorAddCtrl",
                    controllerAs: 'vm',
                    size: 'lg',
                    resolve:{
                        majorId: function(){
                            return majorId;
                        }
                    }
                };
                $uibModal.open(options).result
                    .then(function(){
                    });
            }
            function remove(id){
                var options = {
                    templateUrl: '/static/app/courseToMajor/courseToMajorDelete.html',
                    controller: "CourseToMajorDeleteCtrl",
                    controllerAs: 'vm',
                    size: 'sm',
                    resolve:{
                        id: function(){
                            return id;
                        }
                    }
                };
                $uibModal.open(options).result
                    .then(function(){
                    });
            }
    });