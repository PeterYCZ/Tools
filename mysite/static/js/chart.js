var sqldata = [1,2,3,4,5]
var data = {
  labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
  series: [
    sqldata,
  ]
};

var options = {
  width: 300,
  height: 200
};

new Chartist.Line('.ct-chart', data, options);
