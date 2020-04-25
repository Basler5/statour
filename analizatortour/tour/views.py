import json
import ast
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import SearchRequest
from django.shortcuts import render  # render_to_response, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from .forms import SearchForm
from .models import SearchRequest, SearchTask
from django.http import JsonResponse


def search(request):
    search = SearchForm()
    if request.method == "POST":
        print("Получен POST на search")
        search = SearchForm(request.POST)
        if search.is_valid():
            print('SearchForm IS VALID')
            record = SearchRequest()
            record.departure_country = str(search.cleaned_data.get("departure_country"))  # RU, BY, KZ, ANY
            record.departure_city = str(search.cleaned_data.get("departure_city"))  # Москва, Казань, Сочи
            record.date_of_departure = str(search.cleaned_data.get("date_of_departure"))
            record.changing_the_departure_date = str(search.cleaned_data.get("changing_the_departure_date"))
            record.destination_country = str(search.cleaned_data.get("destination_country"))
            record.destination_resort = str(search.cleaned_data.get("destination_resort"))
            record.hotel_name = str(search.cleaned_data.get("hotel_name"))
            record.count_of_hotel_stars = str(search.cleaned_data.get("count_of_hotel_stars"))
            record.hotel_rating = str(search.cleaned_data.get("hotel_rating"))
            record.type_of_food = str(search.cleaned_data.get("type_of_food"))
            record.return_date = str(search.cleaned_data.get("return_date"))
            record.changing_return_date = str(search.cleaned_data.get("changing_return_date"))
            record.number_of_adults = str(search.cleaned_data.get("number_of_adults"))
            record.number_of_children = str(search.cleaned_data.get("number_of_children"))
            record.number_of_infants = str(search.cleaned_data.get("number_of_infants"))
            record.direct_flights_only = str(search.cleaned_data.get("direct_flights_only"))
            record.accommodation_at_the_hotel_only = str(search.cleaned_data.get("accommodation_at_the_hotel_only"))

            record.save()

            data = record
            task = SearchTask()
            task.save()
            task.search_id = data.id
            task.input_data = json.dumps({
                "self_id": task.id,
                "departure_country": data.departure_country,
                "departure_city": data.departure_city,
                "date_of_departure": str(data.date_of_departure),
                "changing_the_departure_date": data.changing_the_departure_date,
                "destination_country": data.destination_country,
                "destination_resort": data.destination_resort,
                "hotel_name": data.hotel_name,
                "count_of_hotel_stars": data.count_of_hotel_stars,
                "hotel_rating": data.hotel_rating,
                "type_of_food": data.type_of_food,
                "return_date": str(data.return_date),
                "changing_return_date": data.changing_return_date,
                "number_of_adults": data.number_of_adults,
                "number_of_children": data.number_of_children,
                "number_of_infants": data.number_of_infants,
                "direct_flights_only": data.direct_flights_only,
                "accommodation_at_the_hotel_only": data.accommodation_at_the_hotel_only,
            }, ensure_ascii=False)
            task.save()

            # запуск logic.py в котором происходт запрос занных с целевых сайтов
            # на выходе получаем обработанные данные

            # Как сделать redirect на страницу /rezult/ с передачей туда данных от logic.py {DATA} ???
            return HttpResponseRedirect('/rezult/?search_id={}'.format(record.pk))

        else:
            print('SearchForm is FALSE')

    return render(request, 'tour/search.html', {"search": search})


def last_task_aviasales(request):
    if request.method == "POST":
        data = json.loads(request.body)
        search_self_id = data.get("self_id")
        task = SearchTask.objects.get(id=search_self_id)
        task.output_data_aviasales = data
        task.current_status_aviasales = "finish"
        task.save()
        print("SAVE output_data_aviasales")
        # task.search_task.is_loading_ended = True
        # task.search_task.save()
        return HttpResponse()
    else:
        if SearchTask.objects.filter(current_status_aviasales="new").count():
            older_task = SearchTask.objects.filter(current_status_aviasales="new")[0]
            raw_data_aviasales = older_task.input_data
            older_task.current_status_aviasales = "work"
            older_task.save()
        else:
            raw_data_aviasales = ""
        return HttpResponse(content=raw_data_aviasales)

def get_result_data_ajax_aviasales(request):
    search_id = request.GET.get("search_id")
    search_obj = SearchTask.objects.get(search_id=search_id)
    # aviasales_obj = AviasalesSearchTask.objects.get(search_task=search_obj)
    if search_obj.current_status_aviasales == "finish":
        data_to_render = {
            "current_status": search_obj.current_status_aviasales,
            "data": ast.literal_eval(search_obj.output_data_aviasales),
        }
    else:
        data_to_render = {
            "current_status": search_obj.current_status_aviasales,
        }
    return JsonResponse(data=data_to_render, json_dumps_params={"ensure_ascii": False})
########################################################################################################
def last_task_booking(request):
    if request.method == "POST":
        data = json.loads(request.body)
        search_self_id = data.get("self_id")
        task = SearchTask.objects.get(id=search_self_id)
        task.output_data_booking = data
        task.current_status_booking = "finish"
        task.save()
        print("SAVE output_data_booking")
        # task.search_task.is_loading_ended = True
        # task.search_task.save()
        return HttpResponse()
    else:
        if SearchTask.objects.filter(current_status_booking="new").count():
            older_task = SearchTask.objects.filter(current_status_booking="new")[0]
            raw_data_booking = older_task.input_data
            older_task.current_status_booking = "work"
            older_task.save()
        else:
            raw_data_booking = ""
        return HttpResponse(content=raw_data_booking)

def get_result_data_ajax_booking(request):
    search_id = request.GET.get("search_id")
    search_obj = SearchTask.objects.get(search_id=search_id)
    if search_obj.current_status_booking == "finish":
        data_to_render = {
            "current_status": search_obj.current_status_booking,
            "data": ast.literal_eval(search_obj.output_data_booking),
        }
    else:
        data_to_render = {
            "current_status": search_obj.current_status_booking,
        }
    return JsonResponse(data=data_to_render, json_dumps_params={"ensure_ascii": False})
########################################################################################################
def last_task_tourvisor(request):
    if request.method == "POST":
        data = json.loads(request.body)
        search_self_id = data.get("self_id")
        task = SearchTask.objects.get(id=search_self_id)
        task.output_data_tourvisor = data
        task.current_status_tourvisor = "finish"
        task.save()
        print("SAVE output_data_tourvisor")
        # task.search_task.is_loading_ended = True
        # task.search_task.save()
        return HttpResponse()
    else:
        if SearchTask.objects.filter(current_status_tourvisor="new").count():
            older_task = SearchTask.objects.filter(current_status_tourvisor="new")[0]
            raw_data_tourvisor = older_task.input_data
            older_task.current_status_tourvisor = "work"
            older_task.save()
        else:
            raw_data_tourvisor = ""
        return HttpResponse(content=raw_data_tourvisor)

def get_result_data_ajax_tourvisor(request):
    search_id = request.GET.get("search_id")
    search_obj = SearchTask.objects.get(search_id=search_id)
    if search_obj.current_status_tourvisor == "finish":
        data_to_render = {
            "current_status": search_obj.current_status_tourvisor,
            "data": ast.literal_eval(search_obj.output_data_tourvisor),
        }
    else:
        data_to_render = {
            "current_status": search_obj.current_status_tourvisor,
        }
    return JsonResponse(data=data_to_render, json_dumps_params={"ensure_ascii": False})
########################################################################################################
def get_result_data_ajax_rezult(request):
    search_id = request.GET.get("search_id")
    older_task = SearchTask.objects.get(search_id=search_id)
    if older_task.current_status_aviasales == "finish" and \
            older_task.current_status_booking == "finish" and older_task.current_status_tourvisor == "finish":
        raw_data_aviasales = ast.literal_eval(older_task.output_data_aviasales)
        raw_data_booking = ast.literal_eval(older_task.output_data_booking)
        raw_data_tourvisor = ast.literal_eval(older_task.output_data_tourvisor)
        price_a = int(raw_data_aviasales.get("lowest_price"))
        price_b = int(raw_data_booking.get("rezult_with_tax"))
        price_t = int(raw_data_tourvisor.get("price_for_tour"))
        if price_t > (price_a + price_b):
            header_text = "Выгоднее преобретать перелет + проживание раздельно (не туром)."
            rezult_price = price_a + price_b
            raw_rez_diff = round(((price_t - (price_a + price_b)) / (price_a + price_b)) * 1000)
            rezult_difference = str("дешевле на " + str(raw_rez_diff // 10) + "," + str(raw_rez_diff % 10) + "%")
        else:
            header_text = "Выгоднее преобретать путешествие туром."
            rezult_price = price_t
            raw_rez_diff = round((((price_a + price_b) - price_t) / price_t) * 1000)
            rezult_difference = str("дешевле на " + str(raw_rez_diff // 10) + "," + str(raw_rez_diff % 10) + "%")

        data_to_render = {"current_status": "finish",
                          "header_text": header_text,
                          "rda_lowest_price": raw_data_aviasales.get("lowest_price"),
                          "rdb_rezult_with_tax": raw_data_booking.get("rezult_with_tax"),
                          "rdt_price_for_tour": raw_data_tourvisor.get("price_for_tour"),
                          "rezult_price": str(rezult_price),
                          "rezult_difference": str(rezult_difference),
                       }
        older_task.output_data_rezult = data_to_render
        older_task.current_status_rezult = "finish"
        older_task.save()
    else:
        data_to_render = {
            "current_status": older_task.current_status_rezult,
        }
    return JsonResponse(data=data_to_render, json_dumps_params={"ensure_ascii": False})
########################################################################################################
def rezult(request):
    search_id = request.GET.get("search_id")
    form = get_object_or_404(SearchRequest, pk=search_id)
    if request.method == "POST":
        search = SearchForm(request.POST, instance=form)
        if search.is_valid():
            print('SearchForm IS VALID')
            # form = form.save(commit=False)
            form.departure_country = str(search.cleaned_data.get("departure_country"))  # RU, BY, KZ, ANY
            form.departure_city = str(search.cleaned_data.get("departure_city"))  # Москва, Казань, Сочи
            form.date_of_departure = str(search.cleaned_data.get("date_of_departure"))
            form.changing_the_departure_date = str(search.cleaned_data.get("changing_the_departure_date"))
            form.destination_country = str(search.cleaned_data.get("destination_country"))
            form.destination_resort = str(search.cleaned_data.get("destination_resort"))
            form.hotel_name = str(search.cleaned_data.get("hotel_name"))
            form.count_of_hotel_stars = str(search.cleaned_data.get("count_of_hotel_stars"))
            form.hotel_rating = str(search.cleaned_data.get("hotel_rating"))
            form.type_of_food = str(search.cleaned_data.get("type_of_food"))
            form.return_date = str(search.cleaned_data.get("return_date"))
            form.changing_return_date = str(search.cleaned_data.get("changing_return_date"))
            form.number_of_adults = str(search.cleaned_data.get("number_of_adults"))
            form.number_of_children = str(search.cleaned_data.get("number_of_children"))
            form.number_of_infants = str(search.cleaned_data.get("number_of_infants"))
            form.direct_flights_only = str(search.cleaned_data.get("direct_flights_only"))
            form.accommodation_at_the_hotel_only = str(search.cleaned_data.get("accommodation_at_the_hotel_only"))
            form.save()

            task = SearchTask.objects.get(search_id=search_id)
            task.input_data = json.dumps({
                "self_id": task.id,
                "departure_country": form.departure_country,
                "departure_city": form.departure_city,
                "date_of_departure": str(form.date_of_departure),
                "changing_the_departure_date": form.changing_the_departure_date,
                "destination_country": form.destination_country,
                "destination_resort": form.destination_resort,
                "hotel_name": form.hotel_name,
                "count_of_hotel_stars": form.count_of_hotel_stars,
                "hotel_rating": form.hotel_rating,
                "type_of_food": form.type_of_food,
                "return_date": str(form.return_date),
                "changing_return_date": form.changing_return_date,
                "number_of_adults": form.number_of_adults,
                "number_of_children": form.number_of_children,
                "number_of_infants": form.number_of_infants,
                "direct_flights_only": form.direct_flights_only,
                "accommodation_at_the_hotel_only": form.accommodation_at_the_hotel_only,
            }, ensure_ascii=False)
            task.current_status_aviasales = "new"
            task.current_status_booking = "new"
            task.current_status_tourvisor = "new"
            task.current_status_rezult = "new"
            task.save()
            return HttpResponseRedirect('/rezult/?search_id={}'.format(form.pk))
    else:
        search = SearchForm(instance=form)
    return render(request, 'tour/rezult.html', {"search": search})

def tech(request):

    return render(request, 'tour/tech.html')