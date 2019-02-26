function gaugeChart() {
	$.ajax({
      type: "GET",
      url: "log/templog.csv",
      dataType: "text",
      success: function(response)
      {
      chartData = $.csv.toArrays(response, {onParseValue: $.csv.hooks.castToScalar});
//      console.log(chartData);

      var rows = chartData.length;
      var chartArray = [];

	var g2data = new google.visualization.arrayToDataTable([
              [ {label: 'Temperature', id:'temp', type: 'number'} ]
              ]);
	for (var i = 0; i = row -1; i++) {
          g2data.addRow([chartData[i][6]]);
        }              

    console.log(g2data);

	var options2 = {
          redFrom: 88, redTo: 120,
          yellowFrom:78, yellowTo: 120,
          minorTicks: 5
    };

    var gauge = new google.visualization.Gauge(document.getElementById('gauge'));
    gauge.draw(g2data, options2);

    setInterval(function() {
        data.setValue(0, 1, 40 + Math.round(60 * Math.random()));
        gauge.draw(g2data, options2);
    }, 13000);

    }}); 
}