console.log("test")
document.addEventListener("DOMContentLoaded", function(){
    lastLat = document.querySelector('#id_last_lat')
    if (lastLat){
    var data = document.querySelectorAll(".has_original");
    var coordinates = []
    var latSaved = 0
    data.forEach(function(element) {
        var lat = element.querySelector(".field-lat input").value
        var lng = element.querySelector(".field-lng input").value
            if (Math.abs(latSaved - parseFloat(lat))>0.0005){
                coordinates.push({lat: parseFloat(lat), lng: parseFloat(lng)});
                latSaved = lat;
            }
    })
    console.log(coordinates)
    var lastElement = document.querySelector('#scooteractivity_set-group')
    lastElement.insertAdjacentHTML('beforebegin',
    '<div id="map"></div>');

    var bounds = new google.maps.LatLngBounds();

    var map = new google.maps.Map(document.getElementById('map'), {
        mapTypeId: google.maps.MapTypeId.ROADMAP
   });
   var markers = [];
   coordinates.forEach(function(element,index) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(element.lat, element.lng),
            label: String(index+1),
            map: map
        });
        markers.push(marker)
    })
    var bounds = new google.maps.LatLngBounds();
    for (var i = 0; i < markers.length; i++) {
    bounds.extend(markers[i].getPosition());
    }

    map.fitBounds(bounds);

    var flightPlanCoordinates = coordinates
      var flightPath = new google.maps.Polyline({
        path: flightPlanCoordinates,
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 1.0,
        strokeWeight: 2
      });

      flightPath.setMap(map);

}
})
