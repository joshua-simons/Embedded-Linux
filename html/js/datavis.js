google.charts.load('current', { packages: ['corechart'] });

URL="../log/templog.csv"
var queryOptions= {
   csvColumns: ['date','number','number'],
   csvHasHeader: true
}

   function drawChart() {
      var gdata = new google.visualization.DataTable({

        cols: [ {label: 'Date', id: 'date', type: 'date'},
                {label: 'Temperature', id:'temp', type: 'number'},
                {label: 'Humidity', id:'humid', type: 'number'},
              ],
        rows: [
              {[new Date(2019, 1, 21), 74.5, 6.0]},
              {[new Date(2019, 1, 22), 73.9, 6.3]},
              {[new Date(2019, 1, 23), 73.9, 6.1]},
              {[new Date(2019, 1, 24), 73.9, 6.0]}
              ]
  });
         var options = {
            title: 'Temperture Log',
            curveType: 'function',
            legend: { position: 'bottom' }
         };

         var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

         chart.draw(gdata, options);
           
   }
