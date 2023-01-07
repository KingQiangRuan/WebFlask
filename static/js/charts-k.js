option = {
    xAxis: {
      data: ['1', '2', '3', '4', '5', '6', '7', '8']
    },
    yAxis: {},
    series: [
      {
        type: 'candlestick',
        data: [
          [20, 34, 10, 38],
          [40, 35, 30, 50],
          [31, 38, 33, 44],
          [38, 15, 5, 42],
          [38, 15, 5, 42],
          [37, 25, 13, 55],
          [43, 18, 15, 58],
          [38, 23, 8, 60]
        ]
      }
    ]
  };

var myChart = echarts.init(document.getElementById('k_Chart'),
null,
{ //设置控制图表大小变量
    width: 420,
    height: 300
});
myChart.setOption(option);