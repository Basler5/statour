import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import datetime
import re

# departure_country = str(RU)  # RU, BY, KZ, ANY
# departure_city = str(Москва)  # Москва, Казань, Сочи
date_of_departure = "2020-05-18"
# changing_the_departure_date = str(var_day_0)
# destination_country = str(TH)
destination_resort = "рим"
hotel_name = ""
count_of_hotel_stars = "4"
hotel_rating = "7"
type_of_food = "2"
return_date = "2020-05-20"
# changing_return_date = str(var_day_0)
number_of_adults = "2"
number_of_children = "2"
number_of_infants = "0"
# direct_flights_only = str(True)
accommodation_at_the_hotel_only = True

def search_booking(date_of_departure=date_of_departure,
                    destination_resort=destination_resort,
                    hotel_name=hotel_name,
                    count_of_hotel_stars=count_of_hotel_stars,
                    hotel_rating=hotel_rating,
                    type_of_food=type_of_food,
                    return_date=return_date,
                    number_of_adults=number_of_adults,
                    number_of_children=number_of_children,
                    number_of_infants=number_of_infants,
                    accommodation_at_the_hotel_only=accommodation_at_the_hotel_only,
                   ):

    # Инициализация запроса ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    booking_name_hotel = ''
    booking_count_of_hotel_stars = ''
    booking_adress_hotel = ''
    booking_hotel_rating = ''
    booking_type_of_food = 'Питание не включено в стоимость'
    booking_type_of_room = []
    booking_price = ''
    booking_price_taxes = ''

    url = 'https://www.booking.com/searchresults.ru.html'
    if hotel_name:
        url += ("?ss=" + destination_resort + "%2C+" + hotel_name.replace(' ', '+'))
    else:
        url += ("?ss=" + destination_resort)
    url += ("&checkin_year=" + str(date_of_departure.year))
    url += ("&checkin_month=" + str(date_of_departure.month))
    url += ("&checkin_monthday=" + str(date_of_departure.day))
    url += ("&checkout_year=" + str(return_date.year))
    url += ("&checkout_month=" + str(return_date.month))
    url += ("&checkout_monthday=" + str(return_date.day))
    url += ("&group_adults=" + str(number_of_adults))
    url += ("&group_children=" + str(int(number_of_children) + int(number_of_infants)))

    if not hotel_name:
        url += ("&no_dorms=1")
        url += ("&order=price")
        if int(count_of_hotel_stars) or int(type_of_food) or int(hotel_rating) or accommodation_at_the_hotel_only:
            url += "&nflt=rpt%3D1%3B"
            if int(count_of_hotel_stars):
                for i in range(int(count_of_hotel_stars), 6):
                    url += ("class%3D" + str(i) + "%3B")
            if int(type_of_food):
                if str(type_of_food) == '2':
                    url += ("mealplan%3D" + "1" + "%3B")
                    url += ("mealplan%3D" + "9" + "%3B")
                    url += ("mealplan%3D" + "3" + "%3B")
                    url += ("mealplan%3D" + "4" + "%3B")
                if str(type_of_food) == '3':
                    url += ("mealplan%3D" + "9" + "%3B")
                    url += ("mealplan%3D" + "3" + "%3B")
                    url += ("mealplan%3D" + "4" + "%3B")
                if str(type_of_food) == '4':
                    url += ("mealplan%3D" + "3" + "%3B")
                    url += ("mealplan%3D" + "4" + "%3B")
                if str(type_of_food) == '5':
                    url += ("mealplan%3D" + "4" + "%3B")
            if int(hotel_rating):
                url += ("review_score%3D" + str(int(hotel_rating) * 10) + "%3B")
            if accommodation_at_the_hotel_only:
                url += ("ht_id%3D204%3B")

    print(url)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/User/djangosite/tour/chromedriver.exe")
    driver.get(url)
    # time.sleep(20)

    html = driver.page_source
    # time.sleep(5)
    # print(driver.page_source)
    new_html = html[html.find("sr-hotel__name"):html.find('</a>\n</div>\n</div>\n</div>\n</div>\n</div>')]
    try:
        stars = new_html.split('<span class="invisible_spoken">')[2].split("</span>")[0]
        if len(stars) > 30:
            booking_count_of_hotel_stars = 'Информации о звездах нет. Только рейтинг, ' \
                                           'выставленый самим вариантом размещения.'
        else:
            booking_count_of_hotel_stars = stars
    except Exception:
        print('ОШИБКА - Сведения о звездности отеля не найдены')
    try:
        booking_name_hotel = new_html.split("\n</span>")[0].split('">\n')[1]
    except Exception:
        print('ОШИБКА - Сведения о названии отеля не найдены')
    try:
        booking_adress_hotel = re.compile(r'<[^>]+>').sub('', new_html.split(
            '<div class="sr_card_address_line">')[1].split("</div>")[0]).replace(
            '\n\n\n\n\n\n', ';').replace('Показать на карте', '').replace(
            '\n\n\n', ';').replace('\n', '').replace(';;', ';').replace(';', '; ')[1:]
    except Exception:
        print('ОШИБКА - Сведения об адресе отеля не найдены')
    try:
        booking_hotel_rating = new_html.split('aria-label="')[1].split('">')[0]
    except Exception:
        print('ОШИБКА - Сведения о рейтинге отеля не найдены')
    try:
        if new_html.split('\n</h4>')[0].split(">\n")[-1]:
            booking_type_of_room.append(new_html.split('\n</h4>')[0].split(">\n")[-1] + ':')
        for i in range(1, len(new_html.split('<div class="roomNameInner">'))):
            booking_type_of_room.append(re.compile(r'<[^>]+>').sub('', new_html.split(
                '<div class="roomNameInner">')[i].split("\n</span>")[0].replace(
                '&nbsp;', ' ')).replace('\n', '').replace(' — ', ''))
    except Exception:
        print('ОШИБКА - Сведения о типе номера отеля не найдены')
    try:
        booking_price = new_html.split('<span class="bui-u-sr-only">\nЦена\n')[-1].split(
            '&nbsp;руб.\n</span>')[0].replace(' ', '')
    except Exception:
        print('ОШИБКА - Сведения о стоимости отеля не найдены')
    try:
        booking_price_taxes = new_html.split('prd-taxes-and-fees-under-price')[-1].split('</div>')[0].split('> ')[1]
        try:
            booking_price_taxes2 = booking_price_taxes.replace(' ', '').split('сборы(')[1].split('&nbsp;руб.')[0]
        except Exception:
            print('Сумма налога не найдена')
        else:
            booking_price_taxes = int(booking_price_taxes2)
    except Exception:
        print('ОШИБКА - Сведения о налогах отеля не найдены')
    try:
        food_html = html[html.find("sr_item_default"):html.find(booking_name_hotel)]
        try:
            booking_type_of_food = food_html.split('add-red-tag__amount--small">\n')[1].split("\n<span")[0]
        except Exception:
            print('Сведения о типе питания не найдены')
    except Exception:
        print('ОШИБКА - Сведения о питании отеля не найдены')

    rezult = ["Название отеля: " + booking_name_hotel,
              "Кол-во звезд отеля: " + booking_count_of_hotel_stars,
              "Расположение отеля: " + booking_adress_hotel,
              "Рейтинг отеля: " + booking_hotel_rating,
              "Тип питания: " + booking_type_of_food,
              booking_type_of_room,
              "Цена за отель: " + booking_price,
              "Налоги и сборы: " + str(booking_price_taxes),
              ]

    if type(booking_price_taxes) is int:
        rezult.append("ИТОГО с налогами: " + str(int(booking_price) + int(booking_price_taxes)))
    else:
        rezult.append("ИТОГО с налогами: " + str(booking_price))
    driver.quit()
    return rezult
