$(document).ready(function(){
var i = 0, howManyTimes = 18;
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
                            $("<table class='col'>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">Путешествие в <strong>" + rez.data.destination_resort +
                                "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Самое выгодное место проживания в</td>\n" +
                                "<td><strong>" + rez.data.rez_hotel_name + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Кол-во звезд места проживания:</td>\n" +
                                "<td><strong>" + rez.data.stars + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Район места проживания:</td>\n" +
                                "<td><strong>" + rez.data.location + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Рейтинг места проживания (от 0 до 5):</td>\n" +
                                "<td><strong>" + rez.data.overall_rating + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Питание включенное в тур:</td>\n" +
                                "<td><strong>" + rez.data.rez_type_of_food + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Сведения о типе размещения:</td>\n" +
                                "<td><strong>" + rez.data.rez_type_of_room + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Туроператор: </td>\n" +
                                "<td><img src=\"http://" + rez.data.link_to_the_tour_operator + "\" width=\"160\" height=\"64\" alt=\"tour_operator\">" +
                                "</td></tr>\n" +
                                "</table>")
                            );
                    $("div[name='page_tourvisor_price']").empty();
                    $("div[name='page_tourvisor_price']").append(
                            $("<span class=\"h2\">\n" +
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
    else{
        if(howManyTimes != 0){
            $("div[name='page_tourvisor']").empty();
            $("div[name='page_tourvisor']").append(
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




