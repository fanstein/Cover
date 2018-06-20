//根据窗口调整表格高度
    $(window).resize(function() {
        $('#mytab').bootstrapTable('resetView', {
            height: tableHeight()
        })
    });
//生成用户数据
    $('#mytab').bootstrapTable({
        method: 'get',
        contentType: "application/x-www-form-urlencoded",//必须要有！！！！
        url:'/dailywork/result',//要请求数据的文件路径
        height:tableHeight(),//高度调整
        toolbar: '#toolbar',//指定工具栏
        striped: true, //是否显示行间隔色
        editable:true,
        showPaginationSwitch:true,
        dataField: "rows",//bootstrap table 可以前端分页也可以后端分页，这里
        //我们使用的是后端分页，后端分页时需返回含有total：总记录数,这个键值好像是固定的  
        //rows： 记录集合 键值可以修改  dataField 自己定义成自己想要的就好
        pageNumber: 1, //初始化加载第一页，默认第一页
        pagination:true,//是否分页
        queryParamsType:'limit',//查询参数组织方式
        queryParams:queryParams,//请求服务器时所传的参数
        sidePagination:'server',//指定服务器端分页
        pageSize:10,//单页记录数
        pageList:[5,10,20,30],//分页步进值
        showRefresh:true,//刷新按钮
        showColumns:true,
        search:true,
        clickToSelect: true,//是否启用点击选中行
        toolbarAlign:'right',//工具栏对齐方式
        buttonsAlign:'right',//按钮对齐方式
        columns:[
            {
                title:'全选',
                field:'select',
                //复选框
                checkbox:true,
                width:25,
                align:'center',
                valign:'middle'
            },
            {
                title:'ID',
                field:'id',
                visible:false
            },
            {
                title:'应用和接口',
                field:'name',
                sortable:true
            },
            {
                title:'平均响应时间',
                field:'time',
                sortable:true
            },
            {
                title:'TPS',
                field:'TPS',
                sortable:true
            },
            {
                title:'成功率',
                field:'success',
                sortable:true
            },
            {
                title:'执行日期',
                field:'create_time',
                sortable:true
            },
            {
                title:'操作',
                field:'attribute',
                align:'center',
                //列数据格式化
                formatter:operateFormatter
            }
        ],
        locale:'zh-CN',//中文支持,
        responseHandler:function(res){
            //在ajax获取到数据，渲染表格之前，修改数据源
            return res;
        }
    });
    // //三个参数，value代表该列的值
    // function operateFormatter(value,row,index){
    //     if(value==2){
    //         return '<i class="fa fa-lock" style="color:red"></i>'
    //     }else if(value==1){
    //         return '<i class="fa fa-unlock" style="color:green"></i>'
    //     }else{
    //         return '数据错误'
    //     }
    // }

    function operateFormatter(value,row,index){
        let strHtml;
        strHtml = '<a href="./index.php?r=subprocess/modify&id=' + row.id + '">' +
            '<li class="glyphicon glyphicon-pencil"></li></a>' +
            '<a href="javascript:void(0);" onclick="removeData(' + index + ')" style="margin-left:5px;"><li class="glyphicon glyphicon-remove"></li></a>';
        return strHtml;
    }

    //请求服务数据时所传参数
    function queryParams(params){
        return{
            //每页多少条数据
            pageSize: params.limit,
            //请求第几页
            pageIndex:params.pageNumber,
            Name:$('#search_name').val(),
            Tel:$('#search_tel').val()
        }
    }
     //查询按钮事件
    $('#search_btn').click(function(){
        $('#mytab').bootstrapTable('refresh', {url: '/dailywork/result'});
    });
    //编辑
    $('#btn_edit').click(function(){
        // $('#mytab').bootstrapTable('getSelections');
        $('#mytab').bootstrapTable('updateRow', {index:'getSelections', row :row});
    });
    //删除
    $('#btn_delete').click(function(){
        $('#mytab').bootstrapTable('refresh', {url: '/dailywork/result'});
    });
    //新增
    $('#btn_add').click(function(){
        $('#mytab').bootstrapTable('refresh', {url: '/dailywork/result'});
    });
    //tableHeight函数
    function tableHeight(){
        //可以根据自己页面情况进行调整
        return $(window).height() -280;
    }