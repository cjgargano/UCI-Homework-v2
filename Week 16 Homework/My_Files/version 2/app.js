// Create the svg Viewport
var svgWidth = 960;
var svgHeight = 500;

var margin = { top: 20, right: 40, bottom: 80, left: 100 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svgContainer = d3
  .select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

 // Append an SVG group
var chart = svgContainer.append("g");


// Circle Data Set
// NEED TO FIGURE THIS PART OUT...
// HOW DO I GET MY DATA INTO SAME FORMAT AS THE EXAMPLE?
// OR HOW CAN I MAKE THE EXAMPLE WORK WITH MY DATA?
// var circleData = d3.csv("healthData.csv");

var circleData = d3.csv("healthData.csv", function(error, healthData) {
	if (error) throw error;

	healthData.forEach(function(data) {
		data.inPoverty = +data.inPoverty;
		data.noCoverage = +data.noCoverage;
	});

	// Create scale functions
	var yLinearScale = d3.scaleLinear().range([height, 0]);
	var xLinearScale = d3.scaleLinear().range([0, width]);

	// Create axis functions
	var bottomAxis = d3.axisBottom(xLinearScale);
	var leftAxis = d3.axisLeft(yLinearScale);

	// Create variables to store the min and max values in a column in data.csv
	var xMin;
	var xMax;
	var yMax;

	// Assign values to xMin, xMax abd yMax variables, which will define the axis domain
  	xMin = d3.min(healthData, function(data) {
  		return +data.inPoverty * 0.8;
  	});

  	xMax = d3.max(healthData, function(data) {
  		return +data.inPoverty * 1.1;
  	});

  	yMax = d3.max(healthData, function(data) {
  		return +data.noCoverage * 1.1;
  	});

  	// Set the domain of an axis to extend from the min to the max vaule of the data column
  	xLinearScale.domain([xMin, xMax]);
  	yLinearScale.domain([0, yMax]);

  	// Initialize tooltip
  	var toolTip = d3
  		.tip()
  		.attr("class", "tooltip")
  		.offset([75, -75])
  		.html(function(data) {
  			var state = data.state;
  			var noCoverage = +data.noCoverage;
  			var inPoverty = +data.inPoverty
  			return state + 
  			"<br> % in Poverty: " + inPoverty + 
  			"<br> % w/o Coverage: " + noCoverage
  		});

  	// Create tooltip
  	chart.call(toolTip);

  	// Draw the circles
  	chart
  		.selectAll("circle")
  		.data(healthData)
  		.enter()
  		.append("circle")
  		.attr("cx", function(data, index) {
  			return xLinearScale(+data.inPoverty);
  		})
  		.attr("cy", function(data, index) {
  			return yLinearScale(data.noCoverage);
  		})
		.attr("text", function(data) {
			return data.abbr;
		})
  		.attr("r", "12")
  		.attr("fill", "#e86400") // Orange
  		.attr("stroke", "#000000") // Black
  		.attr("opacity", 0.8)
  		//.attr("")
  		// display tooltip on click
  		.on("mouseover", function(data) {
  			toolTip.show(data);
  		})
  		// hide tooltip on mouseout
  		.on("mouseout", function(data, index) {
  			toolTip.hide(data);
  		});

	// Add Text Element to the "g" Element
	var text = chart.selectAll("text")
	  				.data(healthData)
	  				.enter()
	  				.append("text");

	// Append state abbreviations
	var textLabels = text
					.attr("x", function(data, index) {
						// X-coordinate where text should start
					  	return xLinearScale(+data.inPoverty) - 6;
					})
					.attr("y", function(data, index) {
						// Y-coordinate where text should start				  			
						return yLinearScale(data.noCoverage) + 3;
					})
					.text(function(data) {
						return data.abbr;
					})
					.attr("font-family", "sans-serif")
					.attr("font-size", "9px")
					.attr("fill", "black");

  	// Append an SVG group for the x-axis, then display the x-axis
  	chart
  		.append("g")
  		.attr("transform", "translate(0," + height + ")")
  		.attr("class", "x-axis")
  		.call(bottomAxis);

  	// Append a group for y-axis, then display it
  	chart
  		.append("g")
  		.call(leftAxis);

  	// Append y-axis label
  	chart
  		.append("text")
  		.attr("transform", "rotate(-90)")
  		.attr("y", 0 - margin.left + 40)
  		.attr("x", 0 - height / 1.25)
  		.attr("dy", "1em")
  		.attr("class", "axis-text")
  		.attr("data-axis-name", "noCoverage")
  		.text("% Without Healthcare Coverage")

  	// Append x-axis labels
  	chart
  		.append("text")
  		.attr("transform", "translate(" + width / 2.75 + ", " + (height + margin.top + 20) + ")")
  		.attr("class", "axis-text active")
  		.attr("data-axis-name", "inPoverty")
  		.text("% Below the Poverty Line");

});
