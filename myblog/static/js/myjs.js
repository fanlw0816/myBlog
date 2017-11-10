/**
 * Created by python on 17-9-27.
 */

window.onload = function() {
    //加载直接运行一次,解决延缓问题
    clock();
    // 设置定时器，会延缓1秒显示
    setInterval(clock, 1000);
    //获取本地时间
    function clock() {
        var now = new Date();
        var year = now.getFullYear();
        // 月份从0开始计算的
        var month = now.getMonth();
        var date = now.getDate();
        // 星期从 0-6
        var day = now.getDay();
        var hour = now.getHours();
        var minute = now.getMinutes();
        var second = now.getSeconds();

        var oBox = document.getElementById('box');
        oBox.innerHTML = year + "-" + format(month + 1) + "-" + format(date) + "&nbsp;&nbsp;" + week(day) + "&nbsp;&nbsp;" + format(hour) + ":" + format(minute) + ":" + format(second);
    }


    //判断星期几
    function week(day) {
        switch (day) {
            case 0:
                return "Sunday";
                break;
            case 1:
                return "Monday";
                break;
            case 2:
                return "Tuesday";
                break;
            case 3:
                return "Wednesday";
                break;
            case 4:
                return "Thursday";
                break;
            case 5:
                return "Friday";
                break;
            case 6:
                return "Saturday";
                break;
            default:
                break;
        }
    }

    // 用来在个位数时前面添加一个0
    function format(params) {
        if (params < 10) {
            return "0" + params;
        }
        else {
            return params;
        }
    }
};

// 置顶
$(function(){
    var $back = $('.back');
    $(window).scroll(function () {
        var iScrollTop = $(document).scrollTop();
        if (iScrollTop>=500)
            {
                $back.slideDown();
            }
        else
            {
                $back.slideUp();
            }
    })
    $back.click(function () {
        $("html,body").animate({"scrollTop":0});
    })
})