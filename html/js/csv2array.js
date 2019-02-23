//Use ajax to read the csv file as text, and the jquery-csv library to convert it to the array 'data'.
//To make sure it works, log the array to the console
function readCSV() {

	var data;
		$.ajax({
		  type: "GET",
		  url: "log/templog.csv",
		  dataType: "text",
		  success: function(response)
		  {
			data = $.csv.toArrays(response);
			console.log(data);
		  }
		});
}
