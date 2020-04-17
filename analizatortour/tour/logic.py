from tour.aviasales import search_aviasales
from tour.booking import search_booking
from tour.tourvisor import search_tourvisor

            departure_country = str(search.cleaned_data.get("departure_country"))  # RU, BY, KZ, ANY
            departure_city = str(search.cleaned_data.get("departure_city"))  # Москва, Казань, Сочи
            date_of_departure = str(search.cleaned_data.get("date_of_departure"))
            changing_the_departure_date = str(search.cleaned_data.get("changing_the_departure_date"))
            destination_country = str(search.cleaned_data.get("destination_country"))
            destination_resort = str(search.cleaned_data.get("destination_resort"))
            hotel_name = str(search.cleaned_data.get("hotel_name"))
            count_of_hotel_stars = str(search.cleaned_data.get("count_of_hotel_stars"))
            hotel_rating = str(search.cleaned_data.get("hotel_rating"))
            type_of_food = str(search.cleaned_data.get("type_of_food"))
            return_date = str(search.cleaned_data.get("return_date"))
            changing_return_date = str(search.cleaned_data.get("changing_return_date"))
            number_of_adults = str(search.cleaned_data.get("number_of_adults"))
            number_of_children = str(search.cleaned_data.get("number_of_children"))
            number_of_infants = str(search.cleaned_data.get("number_of_infants"))
            direct_flights_only = str(search.cleaned_data.get("direct_flights_only"))
            '''a_s = detect_low_price_aviasales(
                departure_country=departure_country,
                departure_city=departure_city,
                date_of_departure=date_of_departure,
                changing_the_departure_date=changing_the_departure_date,
                destination_country=destination_country,
                destination_resort=destination_resort,
                return_date=return_date,
                changing_return_date=changing_return_date,
                number_of_adults=number_of_adults,
                number_of_children=number_of_children,
                number_of_infants=number_of_infants,
                direct_flights_only=direct_flights_only,
            )'''