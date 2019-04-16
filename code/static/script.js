var map, infoWindow;
// function creates a map to put into browser
function createMap () {
  var directionsService = new google.maps.DirectionsService();
  var directionsDisplay = new google.maps.DirectionsRenderer();
  var options = {
    center: { lat: -33.8688, lng: 151.2093 },
    zoom: 10
  };                   
  
  map = new google.maps.Map(document.getElementById('map'), options);
  directionsDisplay.setMap(map);
   
  // ==== handles geolocation ====
  infoWindow = new google.maps.InfoWindow;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (p) {
        var position = {
            lat: p.coords.latitude,
            lng: p.coords.longitude
        };
        infoWindow.setPosition(position);
        infoWindow.setContent('Your location!');
        infoWindow.open(map);
    }, function () {
        handleLocationError('Geolocation service failed', map.center());

    })
  } else {
    handleLocationError('No geolocation available', map.center());

  }

 // =================================
 // ==== Search ====
  var input = document.getElementById('search');
  var searchBox = new google.maps.places.SearchBox(input);

  map.addListener('bounds_changed', function() {
    searchBox.setBounds(map.getBounds());
  });

  var markers = [];
  
  searchBox.addListener('places_changed', function () {
    var places = searchBox.getPlaces();

    if (places.length == 0)
      return;

    markers.forEach(function (m) { m.setMap(null); });
    markers = [];

    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(p) {
      if (!p.geometry)
        return;

      markers.push(new google.maps.Marker({
        map: map,
        title: p.name,
        position: p.geometry.location
      }));

      if (p.geometry.viewport)
        bounds.union(p.geometry.viewport);
      else
        bounds.extend(p.geometry.location);
    });
    
    map.fitBounds(bounds);
  });
}  

function calcRoute() {
  var selectedMode = document.getElementById('mode').value;
  var request = {
      origin: haight,
      destination: oceanBeach,
      // Note that Javascript allows us to access the constant
      // using square brackets and a string value as its
      // "property."
      travelMode: google.maps.TravelMode[selectedMode]
  };
  directionsService.route(request, function(response, status) {
    if (status == 'OK') {
      directionsDisplay.setDirections(response);
    }
  });
}

function handleLocationError (content, position) {
    infoWindow.setPosition(position);
    infoWindow.setContent(content);
    infoWindow.open(map);


  }
}