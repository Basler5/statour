$(document).ready(function(){
var i = 0, howManyTimes = 300;
f();
function f() {
        var request = new XMLHttpRequest();
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('search_id');
        request.open("GET", "/ajax_tourvisor/?search_id="+id);
        request.send();
        request.onreadystatechange=function(){
            if(this.readyState==4 && this.status==200){
                var rez = JSON.parse(request.responseText);
                if (rez.current_status=="finish"){
                    console.log(rez.data.self_id);
                    howManyTimes = 0;
                    $("div[name='page_tourvisor']").empty();
                        $("div[name='page_tourvisor']").append(
                            $("<table>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">ДИЗАЙН ВЫВОДА В ПРОРАБОТКЕ</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">" + rez.data.rez_hotel_name + "</td>\n" +
                                "</tr>\n" +
                                "</table>")
                            );
                    $("div[name='page_tourvisor_price']").empty();
                    $("div[name='page_tourvisor_price']").append(
                            $("<span class=\"h2 mb-0\">\n" +
                              "Стоимость тура: <strong>" + rez.data.price_for_tour + "</strong>\n" +
                              "</span>\n" +
                              "<span class=\"h2 rubznak-rub text-muted mb-0\"></span>")
                            );
                }
            }
        }
    i++;
    if( i < howManyTimes ){
        setTimeout( f, 5000 );
    }
}
});




