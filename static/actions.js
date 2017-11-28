// weather template

var input = document.getElementById('autocomplete');
var autocomplete = new google.maps.places.Autocomplete(input,{types: ['(cities)']});
var msg = "";
var murl = "";

google.maps.event.addListener(autocomplete, 'place_changed', function(msg){
place = autocomplete.getPlace();
address = new String(place.formatted_address);
splitted = address.split(",");
city = new String(splitted[0].replace(/ /g,"_"));
stateCountry = new String(splitted[1].replace(/\s+/g, '').replace(/[0-9]/g, ''));
msg = new String(stateCountry + "/" + city);
murl = new String("http://api.wunderground.com/api/cb89ade5f98c2a45/geolookup/conditions/forecast/q/" + msg + ".json");

function text() {
    alert(murl);
$.ajax({
  url : murl,
  dataType : "jsonp",
  success : function(parsed_json) {
  var location = parsed_json['location']['city'];
  var temp = parsed_json['current_observation']['temp_c'];
  var feelslike = parsed_json['current_observation']['feelslike_c'];
  var x = 0;
  var day;

  $('#articleHead').append("Weather in " + location + ", " + stateCountry);

  $('#stage').append("Currently in " + location + " it is: " + temp + " degrees");

  if(temp != feelslike) {
    $('#stage').append("But it feels like " + feelslike + " degrees");
  }

  if(temp < 9) {
    $('#stage').append( "Brrr! It's pretty cold. Better bring a jacket to stay warm.");
  }
  if(temp > 23 ) {
    $('#stage').append("Is it just the weather or did you just walk in? Either case, it's hot right now. Stay cool!");
  } 
  $('#stage').append("Here's what is happening in the next 4 days:");

  while (x < 4) {
    day = parsed_json['forecast']['simpleforecast']['forecastday'][x]
    $('#stage').append(day['date']['weekday'] + "," + day['date']['monthname'] + " " + day['date']['day'] + ":");
    $('#stage').append("Conditions: " + day['conditions']);
    $('#stage').append("High: " + day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C");
    $('#stage').append(" ");
    x++;
  }        
}
});
} // end of function

})
