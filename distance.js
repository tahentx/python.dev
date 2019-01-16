
var unirest = require('unirest');

var lat1 = 33.850455;
var long1 = -118.140378;
var lat2 = 34.184308;
var long2 = -118.888122;

unirest.get("https://010pixel-distance-v1.p.rapidapi.com/?unit=K&lat1=10&long1=-25.3&lat2=34.5&long2=-403.4")
.header("X-RapidAPI-Key", "54bfa778e0msh52ed7af4b6f98cfp18b709jsnbc0ccec09a9c")
.end(function (result) {
  console.log(result.status, result.headers, result.body);
});