function bindvercodeClick(){
    $("#verification").on("click",function(event){
        // 通过js发送网络请求：ajax。Async JavaScript And XML（JSON）
        $.ajax({
            url: "/user/vercode",
            method: "GET",
        })
    });
}


// 等网页文档所有元素都加载完成后再执行
$(function () {
    bindvercodeClick();
});