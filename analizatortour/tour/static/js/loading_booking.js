$(document).ready(function(){
var i = 0, howManyTimes = 18;
f();
function f() {
        var request = new XMLHttpRequest();
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('search_id');
        request.open("GET", "/ajax_booking/?search_id="+id);
        request.send();
        request.onreadystatechange=function(){
            if(this.readyState==4 && this.status==200){
                var rez = JSON.parse(request.responseText);
                if (rez.current_status=="finish"){
                    console.log(rez.data.self_id);
                    howManyTimes = 0;
                    $("div[name='page_booking']").empty();

                    $("div[name='page_booking']").append(
                        $("<table class='col'>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\">Проживание в <strong>" + rez.data.destination_resort +
                                "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Самое выгодное место проживания в</td>\n" +
                                "<td><strong>" + rez.data.booking_name_hotel + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Кол-во звезд места проживания:</td>\n" +
                                "<td><strong>" + rez.data.booking_count_of_hotel_stars + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Район места проживания:</td>\n" +
                                "<td><strong>" + rez.data.booking_adress_hotel + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Рейтинг места проживания (от 0 до 10):</td>\n" +
                                "<td><strong>" + rez.data.booking_hotel_rating + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Питание в месте проживания:</td>\n" +
                                "<td><strong>" + rez.data.booking_type_of_food + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Сведения о типе размещения:</td>\n" +
                                "<td><strong>" + rez.data.booking_type_of_room + "</strong></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Стоимость за проживание: </td>\n" +
                                "<td><strong>" + rez.data.booking_price + "</strong>" +
                                "<span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span></td>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Налоги: </td>\n" +
                                "<td><strong>" + rez.data.booking_price_taxes + "</strong>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "</table>")
                        );

                    $("div[name='page_booking_price']").empty();
                    $("div[name='page_booking_price']").append(
                            $("<span class=\"h2\">\n" +
                              "Стоимость проживания с учетом налогов: <strong>" + rez.data.rezult_with_tax + "</strong>\n" +
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
            $("div[name='page_booking']").empty();
            $("div[name='page_booking']").append(
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




