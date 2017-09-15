//var sqldata = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
var sqldata = null;

var elem=document.getElementById("chart1");
  elem.style.position = "relative";
  elem.style.top = "90px"
  elem.style.left = "280px";

function getdata(olddata,newdata){
  sqlolddata = olddata;
  sqlnewdata = newdata

  var data = {
    labels: ['1', '2', '3', '4', '6','7', '8', '9', '10', '11','12','13','14'],
    series: [{
      name: 'olddata',
      data: sqlolddata
    }, {
      name: 'newdata',
      data: sqlnewdata
    },]
  };

  var options = {
    width: 600,
    height: 600,
    chartPadding: { top: 0, right: 0, bottom: 0, left: 0},
    classNames: {
      point: 'ct-point ct-white',
      line: 'ct-line ct-white'
    }
  };

  new Chartist.Line('.ct-chart', data, options);
}
