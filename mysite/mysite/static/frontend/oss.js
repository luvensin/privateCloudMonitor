$(document).ready(function(){
var radius = [40, 60];
option = { 
	    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    toolbox: {
        show : true,
        feature : {
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true, 
                type: ['pie', 'funnel'],
                option: {
                    funnel: {
                        width: '50%',
                        height: '50%',
                        itemStyle : {
                            normal : {
                                label : {
                                    formatter : function (params){
                                        return 'other\n' + params.value + '%\n'
                                    },
                                    textStyle: {
                                        baseline : 'middle'
                                    }
                                }
                            },
                        } 
                    }
                }
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    series : [
        {
        	name :"oss容量",
            type : 'pie',
            radius :'80%',
            x: '10%', // for funnel
            // itemStyle : labelFromatter,
            data : [
                {name:'free', value:1000000},
                {name:'used', value:10456890}
            ]
        }
    ]
};

                

var myChart = echarts.init(document.getElementById('oss_usage'));
myChart.setOption(option);


})

