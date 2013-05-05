<script type="text/javascript">
$(function () {
    var chart;
    $(document).ready(function() {
      var options = ${options | n}
      chart = new Highcharts.Chart(options);
    });
});
</script>
<div id="${renderTo}" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
