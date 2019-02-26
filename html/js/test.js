 $.ajax({
      type: "GET",
      url: "log/templog.csv",
      dataType: "text",
      success: function(response)
      {
      chartData = $.csv.toArrays(response, {onParseValue: $.csv.hooks.castToScalar});
      
 //     console.log(chartData);
      console.log(chartData.length);

      var rows = chartData.length;
      var chartArray = "";

      for (var i = 0; i < rows; i++) {
	      	chartArray += "["+chartData[i][0]+", "+chartData[i][1]+", "+chartData[i][2]+"],";
      }
      chartArray = chartArray.slice(0, -1);
      console.log(chartArray)

      }});