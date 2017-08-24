//var sqldata = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
var sqldata = null;

function getdata(data){
  sqldata = data;
};


var data = {
  labels: ['1', '2', '3', '4', '6','7', '8', '9', '10', '11','12','13','14'],
  series: [
    sqldata,
  ]
};

var options = {
  width: 600,
  height: 600
};

new Chartist.Line('.ct-chart', data, options);
