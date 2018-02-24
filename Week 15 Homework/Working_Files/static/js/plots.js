 // Create a variable that updates based on what the user selected
 // Use event listeners based on what is selected in the drop-down list


// Button Handler
function handleSubmit() {
	// Prevent page from refreshing
	Plotly.d3.event.preventDefault();

	// Select the input value from the form
	var sample_id = Plotly.d3.select("#selDataset").node().value;

	// Clear the input value
	Plotly.d3.select("#selDataset").node().value = "";

	// Update plots with the new sample
	bubblePlot(sample_id);

}

function bubblePlot(sample_id) {
	// var bubble_data = `http://127.0.0.1:5000/api/v1.0/samples/${sample_id}`;
	var bubble_data = `http://127.0.0.1:5000/api/v1.0/samples/BB_940`;
	
	Plotly.d3.json(bubble_data, function(error, response) {

		if (error) return console.warn(error);

		console.log(response);

		// Grab values from the response json object to build the bubble plot
		var trace1 = {
			x: response.otu_list,
			y: response.value_list,
			mode: 'markers',
			marker: {
				size: response.value_list /*,
				color: bubble_color */
			}
		};

		var layout = {
			title: 'Bubble Plot',
			showlegend: false,
			xaxis: 'OTU ID',
			yaxis: 'Sample Value'
		};

		/* var bubble_color = [];
		for (let i = 0; i < otu_list.length; i++) {
			temp_color = rgb(0, 255 * (1 - i/otu_list.length), 255 * (1 - i/otu_list.length));
			bubble_color.push(temp_color);
		}; */

		Plotly.newPlot("bubble-plot", trace1, layout);

	});
}

bubblePlot()


