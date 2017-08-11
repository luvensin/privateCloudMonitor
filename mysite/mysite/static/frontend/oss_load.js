$(document).ready(function(){
      option2 = {
    tooltip : {
        // trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    grid: {
        top: '2%',
        left: '1%',
        right: '2%',
        bottom: '5%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap :false,
            data : ['周一','周二','周三','周四','周五','周六','周日']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'视频广告',
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[1, 2, 2.5, 3, 9, 1, 1.5]
        },
        {
            name:'直接访问',
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[1, 1, 23, 6, 7, 5, 3.5]
        },
        {
            name:'搜索引擎',
            type:'line',
            stack: '总量',
            label: {
                normal: {
                    show: true,
                    position: 'top'
                }
            },
            areaStyle: {normal: {}},
            data:[10, 11, 23, 10, 4, 2, 3]
        }
    ]
};
var yourChart = echarts.init(document.getElementById('avarge_load'));
yourChart.setOption(option2); 
})