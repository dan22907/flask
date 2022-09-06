$(function(){
	//点赞
	$(".liker").on("click",function(){
		// 判断是否已经点赞过
		var num=$(this).html().substring(1)
		if($(this).hasClass("red")){
			$(this).removeClass("red")
			num--
			console.log($(this))
		}else{
			$(this).addClass("red")
			num++
			$(this).html("❤"+num)
			console.log("test1")
		}
	})
})






