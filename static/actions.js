// weather template
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js"></script>
  
  var query;
  jQuery(document).ready(function($) {
    $.ajax({
      url : "http://api.wunderground.com/api/cb89ade5f98c2a45/geolookup/conditions/forecast/q/France/Paris.json",
      dataType : "jsonp",
      success : function(parsed_json) {
        var location = parsed_json['location']['city'];
        var temp = parsed_json['current_observation']['temp_c'];
        var feelslike = parsed_json['current_observation']['feelslike_c'];
        var x = 0;
        var day;

        $('#stage').append("Currently in " + location + " it is: " + temp + " degrees. But it feels like " + feelslike + " degrees");
      
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
  });
 