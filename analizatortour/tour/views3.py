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

def rezult(request):
    search_id = request.GET.get("search_id")
    form = get_object_or_404(SearchRequest, pk=search_id)
    record = SearchRequest.objects.get(id=search_id)
    if request.method == "POST":
        search = SearchForm(request.POST, instance=form)
        if search.is_valid():
            print('SearchForm IS VALID')
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

            task = SearchTask.objects.get(search_id=search_id)
            task.input_data = json.dumps({
                "self_id": task.id,
                "departure_country": record.departure_country,
                "departure_city": record.departure_city,
                "date_of_departure": str(record.date_of_departure),
                "changing_the_departure_date": record.changing_the_departure_date,
                "destination_country": record.destination_country,
                "destination_resort": record.destination_resort,
                "hotel_name": record.hotel_name,
                "count_of_hotel_stars": record.count_of_hotel_stars,
                "hotel_rating": record.hotel_rating,
                "type_of_food": record.type_of_food,
                "return_date": str(record.return_date),
                "changing_return_date": record.changing_return_date,
                "number_of_adults": record.number_of_adults,
                "number_of_children": record.number_of_children,
                "number_of_infants": record.number_of_infants,
                "direct_flights_only": record.direct_flights_only,
                "accommodation_at_the_hotel_only": record.accommodation_at_the_hotel_only,
            }, ensure_ascii=False)
            task.save()

            # запуск logic.py в котором происходт запрос занных с целевых сайтов
            # на выходе получаем обработанные данные

            # Как сделать redirect на страницу /rezult/ с передачей туда данных от logic.py {DATA} ???
            return HttpResponseRedirect('/rezult/?search_id={}'.format(record.pk))
    else:
        search = SearchForm(instance=form)

    record2 = SearchRequest.objects.get(id=search_id)
    data = {
        "departure_country": record2.departure_country,
        "departure_city": record2.departure_city,
        "date_of_departure": record2.date_of_departure,
        "changing_the_departure_date": record2.changing_the_departure_date,
        "destination_country": record2.destination_country,
        "destination_resort": record2.destination_resort,
        "hotel_name": record2.hotel_name,
        "count_of_hotel_stars": record2.count_of_hotel_stars,
        "hotel_rating": record2.hotel_rating,
        "type_of_food": record2.type_of_food,
        "return_date": record2.return_date,
        "changing_return_date": record2.changing_return_date,
        "number_of_adults": record2.number_of_adults,
        "number_of_children": record2.number_of_children,
        "number_of_infants": record2.number_of_infants,
        "direct_flights_only": record2.direct_flights_only,
        "accommodation_at_the_hotel_only": record2.accommodation_at_the_hotel_only,
    }

    return render(request, 'tour/rezult.html', {"search": search})


