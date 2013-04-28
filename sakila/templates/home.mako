<html>
  <head>
    <title>title</title>
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
