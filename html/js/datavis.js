google.charts.load('current', { packages: ['corechart'] });

   function drawChart() {
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

      var gdata = new google.visualization.arrayToDataTable([
              [ {label: 'Date', id: 'date', type: 'date'},
                {label: 'Temperature', id:'temp', type: 'number'},
                {label: 'Humidity', id:'humid', type: 'number'}]
              ]);

        for (var i = 0; i < rows; i++) {
          gdata.addRow([new Date(chartData[i][0],chartData[i][1],chartData[i][2],chartData[i][3],chartData[i][4],chartData[i][5]), chartData[i][6], chartData[i][7]]);
        }              

//        console.log(gdata);

         var options = {
            title: 'Temperture Log',
 //           curveType: 'function',
            legend: { position: 'bottom' }
         };

         var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

         chart.draw(gdata, options);
    }});       
   }
