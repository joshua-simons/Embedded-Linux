//Load the Google Charts packages necessary to use the constructors to make the charts. corechart is the line chart,
//and gauge is the gauge
google.charts.load('current', { packages: ['corechart'] });
google.charts.load('current', {packages:['gauge']});

//This function is called by the onload in the index.html file
function go(){
  drawChart();

//The setInterval function is used to call the drawChart function every 60 seconds (60000 milliseconds) to redraw the chart.
//The xTime variable is set to the date and time when the function is called, and prints it to the console so we know the
//last time the chart was updated.
  
  setInterval(function() {
    xTime = new Date();
    console.clear();
    console.log('Updated Chart: '+xTime);
    drawChart();
    }, 60000);
}

//This function is what reads the csv into an array using ajax (the jquery library)
function drawChart() {
    $.ajax({
      type: "GET",
      url: "log/templog.csv",
      dataType: "text",
      success: function(response)
//Upon success of the GET query, the response is set to the chartData variable, and then parsed to scalar 
//to make the strings into numbers.
      {
      chartData = $.csv.toArrays(response, {onParseValue: $.csv.hooks.castToScalar});

//This sets the variable 'rows' to the number of rows in the chartData array using the javascript function length
      var rows = chartData.length;

//This sets the variable 'gdata' to be out Data Table.  The Data Table is an object created by the constructor
      var gdata = new google.visualization.arrayToDataTable([
//So I am using the arrayToDataTable constructor to create the object, and the array that I am feeding it has the headers
//for the data table hard coded.
        
              [ {label: 'Date', id: 'date', type: 'date'},
                {label: 'Temperature', id:'temp', type: 'number'},
                {label: 'Humidity', id:'humid', type: 'number'}]
              ]);
//Now to populate the Data Table object with the data in the array that I created from the .csv by using an itterative function
//and referrencing the array
        for (var i = 0; i < rows; i++) {
          var fixDate = (chartData[i][1])-1;
          gdata.addRow([new Date(chartData[i][0],fixDate,chartData[i][2],chartData[i][3],chartData[i][4],chartData[i][5]), chartData[i][6], chartData[i][7]]);
        }              

//This sets up the options for the line chart
         var options = {
            title: 'Temperture & Humidity Log',
            curveType: 'function',
            legend: { position: 'bottom' }
         };
//This creates and empty cart object, and tells the browser that the chart will be drawn in the 'curve_chart'
//division defined in the index.html
        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

//This draws the chart using the Data Table stored in gdata and the options defined above
        chart.draw(gdata, options);
        
//This just grabs the last temperature logged in the data array we populated above for the temp to be
//shown on the gauge.  The rest is pretty much the same as above except it draws the gauge.
        var g2data = new google.visualization.arrayToDataTable([
              [ {label: 'Temperature', id:'temp', type: 'number'} ]
              ]);
        lastRow = chartData[chartData.length - 1];
        temp = lastRow[lastRow.length - 2];
        g2data.addRow([temp]);              

        var options2 = {
                redFrom: 88, redTo: 120,
                yellowFrom:78, yellowTo: 120,
                greenFrom:68, greenTo: 120,
                minorTicks: 5
          };

          var gauge = new google.visualization.Gauge(document.getElementById('gauge'));
          gauge.draw(g2data, options2);
    }});      
   }
