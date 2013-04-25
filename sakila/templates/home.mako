<html>
  <head>
    <title>title</title>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <script src="http://code.highcharts.com/highcharts.js" type="text/javascript"></script>
    <script src="http://code.highcharts.com/modules/exporting.js" type="text/javascript"></script>
    <script type="text/javascript">
        $(function () {
            var chart;
            $(document).ready(function() {
                var options = ${options | n}
                chart = new Highcharts.Chart(options);
            });
        });
    </script>
  </head>
  <body>
    <div id="container" style="min-width: 375px; height: 400px; margin: 0 auto"></div>
  </body>
</html>
