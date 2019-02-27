google.charts.load('current', { packages: ['corechart'] });
google.charts.load('current', {packages:['gauge']});

  function update(){
    xTime = new Date();
    console.clear();
    console.log('Updating Charts! '+xTime)
    drawChart();
  }

  function drawChart() {
    $.ajax({
      type: "GET",
      url: "log/templog.csv",
      dataType: "text",
      success: function(response)
      {
      chartData = $.csv.toArrays(response, {onParseValue: $.csv.hooks.castToScalar});
      console.log(chartData);

      var rows = chartData.length;
      var chartArray = [];

      var gdata = new google.visualization.arrayToDataTable([
              [ {label: 'Date', id: 'date', type: 'date'},
                {label: 'Temperature', id:'temp', type: 'number'},
                {label: 'Humidity', id:'humid', type: 'number'}]
              ]);

        for (var i = 0; i < rows; i++) {
          gdata.addRow([new Date(chartData[i][0],chartData[i][1],chartData[i][2],chartData[i][3],chartData[i][4],chartData[i][5]), chartData[i][6], chartData[i][7]]);
        }              

         var options = {
            title: 'Temperture Log',
 //           curveType: 'function',
            legend: { position: 'bottom' }
         };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(gdata, options);
        

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
                blueFrom:0, blueTo:120,
                minorTicks: 5
          };

          var gauge = new google.visualization.Gauge(document.getElementById('gauge'));
          gauge.draw(g2data, options2);

        setInterval(function(){update()
//          lastRow = chartData[chartData.length - 1];
//          temp = lastRow[lastRow.length - 2];
//          g2data.setValue(0,0, temp);
//          gauge.draw(g2data, options2);
        },60000);

    }});      
   }
