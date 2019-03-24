console.log("我就是测试ajax的")
$(document).ready(function () {
    $("#btn").bind("click", function () {
        // console.log("我就是测试的222")
        $.ajax({
            type: "get",
            url: 'ajaxNewsDetail',
            dataType: "json",
            success: function (data, status) {
                // console.log(data)
                // 这个数据的格式是json的,拿出来news是个列表,第i个元素还是列表(见视图里面的数据),所以写成news[i][0]才是新闻
                var news = data['data']
                for (var i = 0; i < news.length; i++) {
                    document.write("<p>标题:" + news[i][0] + "</p>")
                    document.write("<p>作者:" + news[i][1] + "</p>")
                    document.write("<p>添加时间:" + news[i][2] + "</p>")
                    document.write("<hr>")
                }
            }
        })
    })
})