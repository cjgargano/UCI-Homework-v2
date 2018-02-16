// Get references to the tbody element and button for loading additional results
var $tbody = document.querySelector("tbody");
var $loadMoreBtn = document.querySelector("#load-btn");

var $dateInput = document.querySelector("#date");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the $searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredData to the existing table
var filteredData = data;

// renderTable renders the filteredData to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredData.length; i++) {
    // Get the current sighting object and its fields
    var sighting = filteredData[i];
    var fields = Object.keys(sighting);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the sighting object, create a new cell and set its inner text to be the current value at the current sighting's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDate = $dateInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();

  // Set filteredData to an array of all sightings who's "date" and/or shape matches the filter
  filteredData = data.filter(function(sighting) {
    var sightingDate = sighting.datetime.substring(0, filterDate.length).toLowerCase();

    var sightingCity = sighting.city.substring(0, filterCity.length).toLowerCase();    

    var sightingState = sighting.state.substring(0, filterState.length).toLowerCase();

    var sightingCountry = sighting.country.substring(0, filterCountry.length).toLowerCase();

    var sightingShape = sighting.shape.substring(0, filterShape.length).toLowerCase();

    if (sightingDate === filterDate && sightingCity === filterCity && sightingState === filterState && sightingCountry === filterCountry && sightingShape === filterShape) {
      return true;
    }
    return false;
  });
  renderTable();
}

// Set a startingIndex and resultsPerPage variable
var startingIndex = 0;
var resultsPerPage = 50;

function renderTableSection() {
  // Set the value of endingIndex to startingIndex + resultsPerPage
  var endingIndex = startingIndex + resultsPerPage;
  // Get a section of the data array to render
  var dataSubset = data.slice(startingIndex, endingIndex);
  for (var i = 0; i < dataSubset.length; i++) {
    // Get the current sighting object and its fields
    var sighting = dataSubset[i];
    var fields = Object.keys(sighting);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i + startingIndex);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the sighting object, create a new cell and set its inner text to be the current value at the current sighting's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting[field];
    }
  }
}

// Add an event listener to the button, call handleButtonClick when clicked
$loadMoreBtn.addEventListener("click", handleButtonClick);

function handleButtonClick() {
  // Increase startingIndex by 100 and render the next section of the table
  startingIndex += resultsPerPage;
  renderTableSection();
  // Check to see if there are any more results to render
  if (startingIndex + resultsPerPage >= data.length) {
    $loadMoreBtn.classList.add("disabled");
    $loadMoreBtn.innerText = "All sightinges Loaded";
    $loadMoreBtn.removeEventListener("click", handleButtonClick);
  }
}

// Render the table for the first time on page load
renderTableSection();
