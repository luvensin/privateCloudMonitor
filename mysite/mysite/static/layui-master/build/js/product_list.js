

layui.use(['form','layer'], function(){
	var form = layui.form(),
	layer = layui.layer,
	$ = layui.jquery;
  	$('#ecs_table').DataTable({
            // "dom": '<"top">rt<"bottom"flp><"clear">',
            "autoWidth": false,                     // 自适应宽度
            "stateSave": true,                      // 刷新后保存页数
            "order": [[ 1, "desc" ]],               // 排序
            "searching": false,                    // 本地搜索
            "info": true,                           // 控制是否显示表格左下角的信息
            "stripeClasses": ["odd", "even"],       // 为奇偶行加上样式，兼容不支持CSS伪类的场合
            "pagingType": "simple_numbers",         // 分页样式 simple,simple_numbers,full,full_numbers
            "ajax": {
                "url": "/data/ecsdata/"
            },
            "sServerMethod" : "POST",               // POST
            "deferRender": true,                    // 当处理大数据时，延迟渲染数据，有效提高Datatables处理能力
            "columns": [                            // 自定义数据列
                {data: 'sn'},
                {data: 'hostname'},
                {data: 'ip'},
                {data: 'nc_id'},
                {data: 'status'},
                {data: function(obj){
                    return  '<a id="lock"  class="layui-btn layui-btn-small btn-edit" data-id="'+obj.ip+'">锁定</a>' +
                            '<a id="unlock" class="layui-btn layui-btn-small layui-btn-normal btn-edit" data-id="'+obj.ip+'">解锁</a>';
                }}
            ],
            "stateSaveParams": function () {           // 初始化完成调用事件
                // 重新渲染form checkbox 如果你要使用layui的复选框样式打开这个
                form.render('checkbox');
            }
        });	
	  	$(document).on('click','#lock', function(data){
	            // getIds(table对象,获取input为id的属性)
	            var ip_lock = $(this).attr('data-id')
	            $.ajax({
	              type : "POST",
	              dataType : "JSON",
	              url : "/ecs/nc_lock/",
	              data: {"ip":ip_lock},
	              success:function(data){
	                layer.msg(data)
	              },
	              error:function(e){
	                layer.msg(e.responseText)
	              }
	            });
	        });
	  	$(document).on('click','#unlock',function(data){
            var ip_unlock = $(this).attr('data-id')
            $.ajax({
              type : "POST",
              dataType : "JSON",
              url : "/ecs/nc_unlock/",
              data: {"id":ip_unlock},
              success:function(data){
                layer.msg(data)
              },
              error:function(e){
                layer.msg(e.responseText)
              }
            });
        });

})