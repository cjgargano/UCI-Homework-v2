/* data route */

// JS is only reading the path as a string...not reading the data from Flask
// sample_id = "BB_940";
// console.log(sample_id);

var bubble_url = "/api/v1.0/samples/BB_940";
console.log(bubble_url)

function bubblePlot() {
	
	Plotly.d3.json(bubble_url, function(error, response) {

		console.log(response);
		var trace1 = {
			x: bubble_url.otu_id,
			y: bubble_url.sample_value,
			mode: 'markers'
			// marker: {
			// 	size: bubble_url.sample_values
			// }
		};

		console.log(trace1);
		var data = [trace1];

		var layout = {
			title: 'OTU ID vs. Sample Value',
			showlegend: false,
			height: 600,
			width: 1200
		};

		Plotly.newPlot("bubble-plot", data, layout);
	});
}

bubblePlot();