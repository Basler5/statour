$(document).ready(function(){
var i = 0, howManyTimes = 18;
f();
function f() {
        var request = new XMLHttpRequest();
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('search_id');
        request.open("GET", "/ajax_rezult/?search_id="+id);
        request.send();
        request.onreadystatechange=function(){
            if(this.readyState==4 && this.status==200){
                var rez = JSON.parse(request.responseText);
                if (rez.current_status=="finish"){
                    // console.log(rez.data.self_id);
                    howManyTimes = 0;
                    $("div[name='page_header_rezult']").empty();
                    $("div[name='page_header_rezult']").append(
                        $("<h4 class=\"card-header-title\" >" + rez.header_text + "</h4>"));

                    $("div[name='page_rezult']").empty();

                    $("div[name='page_rezult']").append(
                        $("<table>\n" +
                            "<tr>\n" +
                            "<td colspan=\"3\">ДИЗАЙН ВЫВОДА В ПРОРАБОТКЕ</td>\n" +
                            "</tr>\n" +
                            "<tr>\n" +
                            "<td>" + rez.rda_lowest_price + "</td>\n" +
                            "<td>" + rez.rdb_rezult_with_tax + "</td>\n" +
                            "<td>" + rez.rdt_price_for_tour + "</td>\n" +
                            "</tr>\n" +
                            "<tr>\n" +
                            "</table>")
                        );

                    $("div[name='page_rezult_price']").empty();
                    $("div[name='page_rezult_price']").append(
                         $("<div class=\"col-auto\"><span class=\"h2 mb-0\">" +
                           "Итоговая стоимость: <strong>" + rez.rezult_price + "</strong></span>\n" +
                           "<span class=\"h2 rubznak-rub text-muted mb-0\"></span>\n" +
                           "<span class=\"badge badge-soft-success mt-n1\">" + rez.rezult_difference + "</span></div>")
                            );
                }
            }
        }
    i++;
    if( i < howManyTimes ){
        setTimeout( f, 5000 );
    }
    else{
        if(howManyTimes != 0){
            $("div[name='page_rezult']").empty();
            $("div[name='page_rezult']").append(
                            $("<table>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">ДАННЫЕ НЕ ЗАГРУЗИЛИСЬ</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">ЧТО-ТО ПОШЛО НЕ ТАК...</td>\n" +
                                "</tr>\n" +
                                "</table>")
                            );
        }
    }
}
});




