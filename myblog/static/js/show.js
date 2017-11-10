$(function () {
    var aArr_button = [
        'label-default',
        'label-primary',
        'label-success',
        'label-info',
        'label-warning',
        'label-danger'
    ];
    $.get('/get_tags/', function (datas) {
        var data = datas.datas;
        for (var i=0; i<data.length; i++){
            var btn_style = aArr_button[Math.floor(Math.random()*aArr_button.length)];
            var new_tag = '<a href="/tags/'+data[i].id+'/"><span class="label '+btn_style+'">'+data[i].name+'</span></a>';
            $('.tags-show').append(new_tag);

        }
    });

    $.get('/get_hot/', function (datas) {
        var data = datas.datas;
        for (var i=0; i<data.length; i++){
            var new_tag = '<li><a href="/blog/'+data[i].id+'/">'+data[i].title+'</a></li>'
            $('.later-show ol').append(new_tag);
        }
    })
});