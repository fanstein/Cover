function bs_input_file() {
	$(".input-file").before(
		function() {
			if ( ! $(this).prev().hasClass('input-ghost') ) {
				var element = $("<input type='file' class='input-ghost' style='visibility:hidden; height:0'>");
				element.attr("name",$(this).attr("name"));
				element.change(function(){
					element.next(element).find('input').val((element.val()).split('\\').pop());
				});
				$(this).find("button.btn-choose").click(function(){
					element.click();
				});
				$(this).find("button.btn-reset").click(function(){
					element.val(null);
					$(this).parents(".input-file").find('input').val('');
				});
				$(this).find('input').css("cursor","pointer");
				$(this).find('input').mousedown(function() {
					$(this).parents('.input-file').prev().click();
					return false;
				});
				return element;
			}
		}
	);
}
// $(function() {
// 	bs_input_file();
// });

function json_view() {
	var text = document.getElementById('json').value; //获取json格式内容
	try{
        var json;
        json = JSON.stringify(JSON.parse(text), null, 2);//将字符串转换成json对象
    	document.getElementById('json').value = json ;
	}catch(e) {
		document.getElementById('json').value = text ;
	}


}