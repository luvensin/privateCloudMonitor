$(document).ready(function(){
// var labelTop = {
//     normal : {
//         label : {
//             show : true,
//             position : 'center',
//             formatter : '{b}',
//             textStyle: {
//                 baseline : 'bottom'
//             }
//         },
//         labelLine : {
//             show : false
//         }
//     }
// };
// var labelFromatter = {
//     normal : {
//         label : {
//             formatter : function (params){
//                 return 100 - params.value + '%'
//             },
//             textStyle: {
//                 baseline : 'top'
//             }
//         }
//     },
// }
// var labelBottom = {
//     normal : {
//         color: '#ccc',
//         label : {
//             show : true,
//             position : 'center'
//         },
//         labelLine : {
//             show : false
//         }
//     },
//     emphasis: {
//         color: 'rgba(0,0,0,0)'
//     }
// };
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
                {name:'other', value:46},
                {name:'GoogleMaps', value:54}
            ]
        }
    ]
};
                    

var myChart = echarts.init(document.getElementById('oss_usage'));
myChart.setOption(option);

})