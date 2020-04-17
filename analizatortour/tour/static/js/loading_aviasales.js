$(document).ready(function(){
var i = 0, howManyTimes = 18;
f();
function f() {
        var request = new XMLHttpRequest();
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('search_id');
        request.open("GET", "/ajax_aviasales/?search_id="+id);
        request.send();
        request.onreadystatechange=function(){
            if(this.readyState==4 && this.status==200){
                var rez = JSON.parse(request.responseText);
                if (rez.current_status=="finish"){
                    console.log(rez.data.self_id);
                    howManyTimes = 0;
                    $("div[name='page_aviasales']").empty();
                    if (rez.data.airline2_name==""){
                        $("div[name='page_aviasales']").append(
                            $("<table>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">Перелет из " + rez.data.realy_departure_city +
                                " в " + rez.data.realy_destination_resort + "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Найден перелет без пересадок за</td>\n" +
                                "<td><strong>" + rez.data.price_0_transfer + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Найден перелет с одной пересадкой за </td>\n" +
                                "<td><strong>" + rez.data.price_1_transfer + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Найден перелет с двумя пересадками за </td>\n" +
                                "<td><strong>" + rez.data.price_2_transfer + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Самым дешевым является перелет за</td>\n" +
                                "<td><strong>" + rez.data.lowest_price + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Багаж: </td>\n" +
                                "<td><strong>" + rez.data.luggage + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Время направлением ТУДА: </td>\n" +
                                "<td><strong>" + rez.data.time_there + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Время направлением ОБРАТНО: </td>\n" +
                                "<td><strong>" + rez.data.time_back + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td>Авиакомпания: </td>\n" +
                                "<td><img src=\"http://" + rez.data.link1 + "\" width=\"99\" height=\"36\" alt=\"airline1\"></td>\n" +
                                "<td><strong>" + rez.data.airline1_name + "</strong></td>\n" +
                                "</tr>\n" +
                                "</table>")
                            );
                    }
                    else {
                      $("div[name='page_aviasales']").append(
                            $("<table>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">Перелет из <strong>" + rez.data.realy_departure_city +
                                "</strong> в <strong>" + rez.data.realy_destination_resort + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Найден перелет без пересадок за</td>\n" +
                                "<td><strong>" + rez.data.price_0_transfer + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Найден перелет с одной пересадкой за </td>\n" +
                                "<td><strong>" + rez.data.price_1_transfer + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Найден перелет с двумя пересадками за </td>\n" +
                                "<td><strong>" + rez.data.price_2_transfer + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Самым дешевым является перелет за</td>\n" +
                                "<td><strong>" + rez.data.lowest_price + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Багаж: </td>\n" +
                                "<td><strong>" + rez.data.luggage + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Время направлением ТУДА: </td>\n" +
                                "<td><strong>" + rez.data.time_there + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Время направлением ОБРАТНО: </td>\n" +
                                "<td><strong>" + rez.data.time_back + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td>Авиакомпания 1: </td>\n" +
                                "<td><img src=\"http://" + rez.data.link1 + "\" width=\"99\" height=\"36\" alt=\"airline1\"></td>\n" +
                                "<td><strong>" + rez.data.airline1_name + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td>Авиакомпания 2: </td>\n" +
                                "<td><img src=\"http://" + rez.data.link2 + "\" width=\"99\" height=\"36\" alt=\"airline2\"></td>\n" +
                                "<td><strong>" + rez.data.airline2_name + "</strong></td>\n" +
                                "</tr>\n" +
                                "</table>")
                            );
                    };
                    $("div[name='page_aviasales_price']").empty();
                    $("div[name='page_aviasales_price']").append(
                            $("<span class=\"h2 mb-0\">\n" +
                              "Стоимость перелета: <strong>" + rez.data.lowest_price + "</strong>\n" +
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
    else{
        if(howManyTimes != 0){
            $("div[name='page_aviasales']").empty();
            $("div[name='page_aviasales']").append(
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




