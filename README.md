# privateCloudMonitor
app.title = '堆叠柱状图';

option = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['used','sys','wait']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
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
            name:'used',
            type:'bar',
            barWidth : 40,
            color: '#C1232B',
            stack: '搜索引擎',
            data:[0.1, 0.73, 0.70, 0.73, 0.10, 0.11, 0.12]
        },
        {
            name:'sys',
            type:'bar',
            stack: '搜索引擎',
            data:[0.12, 0.13, 0.101, 0.134, 0.290, 0.230, 0.220]
        },
        {
            name:'wait',
            type:'bar',
            stack: '搜索引擎',
            data:[0.62, 0.82, 0.91, 0.84, 0.109, 0.110, 0.120]
        }
    ]
};
