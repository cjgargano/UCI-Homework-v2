// Create map object 
var map = L.map("map", {
    center: [37.763015, -122.459503],
    zoom: 3

});

// Create variable for access token 
var token = "access_token=pk.eyJ1IjoiY2pnYXJnYW5vIiwiYSI6ImNqZTZod2NqazAwaXIyeGxnZXlqYTFkaTMifQ.-LYkZQludov5zH6v7oy-Ww";

// Outdoor Map layer (default)
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" + token).addTo(map);

// Outdoor Map
var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" + token, 
{id: 'map'});

// Satellite Map
var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?" + token,
{id: 'map'});

// Dark Map
var grayscale = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" + token,
{id: 'map'});


var baseMaps = {
    "Outdoors": outdoors,
    "Satellite": satellite,
    "Grayscale": grayscale
};

// Earthquake data
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

var plates = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json"

var controlLayers = L.control.layers(baseMaps).addTo(map);

function styleInfo(feature){
     return{
     fillOpacity: 0.5,
     color: getColor(feature.properties.mag),
     radius: getRadius(feature.properties.mag),
     stroke: true,
     weight: 0.33
    };
};

function getColor(magnitude) {
    if (magnitude <= 1) {
        return "rgb(0, 255, 0)"; // Green
    } else if (magnitude <= 2) {
        return "rgb(51, 204, 0)";
    } else if (magnitude <= 3) {
        return "rgb(102, 153, 0)";
    } else if (magnitude <= 4) { 
        return "rgb(153, 102, 0)";
    } else if (magnitude <= 5) {
        return ("rgb(204, 51, 0");
    } else if (magnitude > 5) {
        return ("rgb(0, 255, 0"); // Red
    } else {
        return ("rgb(255, 255, 255"); // Black (if error)
    }
};

function getRadius(magnitude){
    if (magnitude <= 1) {
        return 3;
    } else if (magnitude <= 2) {
        return 6;
    } else if (magnitude <= 3) {
        return 9;
    } else if (magnitude <= 4) {
        return 12;
    } else if (magnitude <= 5) {
        return 15;
    } else if (magnitude > 5) {
        return 18;
    } else {
        return 0;
    }
};

//Add pop-up for Earthquake Info
function populateInfo(feature, layer) {
    layer.bindPopup("<h1 class='infoHeader'>Earthquake Info</h1> \
    <p class='description'>" + "Location: " + feature.properties.place + "</p>\
    <p class='description'>" + "Magnitude: " + feature.properties.mag + "</p>");
};

function colorPlates(feature){
    return{
        color: "rgb(0, 0, 255", // blue
        fillOpacity: 0.00
    };
};

// function for plate popup
function popPlate(feature, layer) {
    layer.bindPopup("<h1 class='infoHeader'>Tectonic Plate:</h1> \
<p class='plate'>" + feature.properties.PlateName + "</p>");
        
};

// Add GeoJSON layer to the map.
d3.json(link, function(data){
    var earthquakeLayer = L.geoJson(data, {
        // Change each feature into a circleMarker on the map
        pointToLayer: function(feature, latlng) {
          return L.circleMarker(latlng);
        },
        // Set style for each circleMarker using the styleInfo function
        style: styleInfo,
        // Add popup for each marker to display the magnitude and location of the earthquake after the marker has been created and styled
        onEachFeature: populateInfo,       
      }).addTo(map);
      controlLayers.addOverlay(earthquakeLayer, 'Earthquakes');
    });

// add plate layer
d3.json(plates, function(data) {
    // Creating a GeoJSON layer with the retrieved data
    var plateLayer  = L.geoJson(data, {
        style: colorPlates,
        // onEachFeature - popPlate to add popup for each plate
        onEachFeature: popPlate,
    }).addTo(map);
    controlLayers.addOverlay(plateLayer, "Tectonic Plates");

// Setting up the legend
var legend = L.control({position: 'bottomleft'});
legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 1, 2, 3, 4, 5],
        labels = [];

    // Loop through intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i]) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(map);

});
