var app;
app = angular.module("my_app", []);
app.controller("ctrl",function($scope,$http){
	$scope.searchWord=function(search){
	 $http.get("/search/"+search).then(function(response){
		$scope.resp = response.data;
	});
	};

});