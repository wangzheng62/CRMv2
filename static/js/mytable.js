function f1(event) {
    var t=$(event.target.parentNode)
    $("#bgmain").removeClass("invisible");
    $(".active").addClass('mark');
    $(".active").removeClass('active');
    var td1=$(event.target.parentNode).children("td:gt(1)");
    var th1=$("tr:first").children(":gt(1)");
    var i=0,len=th1.length,str="<form class='form-group'>";
    for (;i<len;i++)
    {
        nm=th1[i].getAttribute('name')
        s1="<div class='col-lg-6 col-md-6 col-sm-6 col-xs-6'><label for=" +nm+ "class ='control-label'> " +nm+":</label>"
        s2="<input type='text' class='form-control' name="+nm+" value="+td1[i].innerHTML+"></div>"
        str=str+s1+s2
    }
    str=str+"<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><input type='submit'value='修改'>"+"</form></div>"
    $("#formarea").html(str);
}
function f2(event) {
    var t=$(event.target).text();
    var n=$(event.target).attr("name");
    str=" "+"<input type='text' name="+n+" class='form-text' placeholder="+t+">";
    $("#fliterform").append(str);


}
function f3() {
    var t=$(event.target).val();
    alert(t)

}
function f4() {
    alert(1);
    $(event.target).remove();

}
function selected(event) {

     var t=$(event.target.parentNode);
     t.toggleClass("info")

}
function page(event) {

    var t=$(event.target).text();

    $("li").removeClass('active');
    $(event.target.parentNode).addClass('active');
    $("table").addClass("invisible");
    $('table').eq(t-1).removeClass("invisible");

}
function list(event) {
     alert(document.referrer);
    $(".list-group-item").removeClass('active');
    $(event.target).addClass('active');
}
function selectall() {
    $("td:visible").parent().toggleClass('info');
    
}
function fliter() {
    var d=$("#fliterform").serialize();
    var table_name=$("#fliterform").attr('name');
    d=d+"&tablename="+table_name
    alert(d);
    $.post('test',d,function (data) {
        $("#tablearea").html(data);

    })

}
function rm(event) {

    $("#bgmain").addClass("invisible");
    $(".mark").addClass("active");
    $(".mark").removeClass("mark");


}
$(document).ready(function () {

    $("body").on("dblclick","td",f1);
    $("body").on("click","td",selected);
    $("body").on("dblclick","th:gt(0)",f2);
    $("body").on("dblclick","#fliterform:text",f4);
    $("body").on("click","li",page);
    $("body").on("click",":checkbox",selectall);
    $("body").on("click","button",fliter);
    $("body").on("click",".bg",rm);
})