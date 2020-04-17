import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


departure_country = str('russia')  # departure_country / страна отправления
departure_city = str('MOW')  # departure_city / город отправления
date_of_departure = str('0805')  # date_of_departure / дата отправления
changing_the_departure_date = int(1)  # changing_the_departure_date / изменение даты отправления
destination_country = str('russia')  # destination_country / страна назначения
destination_resort = str('KZN')  # destination_resort / курорт назначения
return_date = str('1306')  # return_date / дата возвращения
changing_return_date = int(1)  # changing_return_date / изменение даты отправления
number_of_adults = str('1')  # number_of_adults / кол-во врослых от 12 лет
number_of_children = str('0')  # number_of_children / кол-во детей от 2х до 12 лет
number_of_infants = str('0')  # number_of_infants / кол-во грудных детей до 2х лет
direct_flights_only = 0

# https://www.aviasales.ru/search/MOW0805KZN13061


def search_aviasales(departure_country = departure_country,
                       departure_city = departure_city,
                       date_of_departure = date_of_departure,
                       changing_the_departure_date = changing_the_departure_date,
                       destination_country = destination_country,
                       destination_resort = destination_resort,
                       return_date = return_date,
                       changing_return_date = changing_return_date,
                       number_of_adults = number_of_adults,
                       number_of_children = number_of_children,
                       number_of_infants = number_of_infants,
                       direct_flights_only = direct_flights_only,
                       ):
    # Инициализация запроса ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    if departure_city == "Москва":
        departure_city = "MOW"
    destination_resort = "KZN"
    sp_date_of_departure = str(date_of_departure).split('-')
    date_of_departure = sp_date_of_departure[2] + sp_date_of_departure[1]
    sp_return_date = str(return_date).split('-')
    return_date = sp_return_date[2] + sp_return_date[1]

    url = 'https://www.aviasales.ru/search/' + departure_city + date_of_departure + destination_resort + return_date + number_of_adults + number_of_children + number_of_infants
    while url[-1] == '0':  # отбрасываем нули из конца запроса, чтобы он был похож на настоящий :))
        url = url[:-1]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(
        options=chrome_options, executable_path="C:/Users/User/djangosite/tour/chromedriver.exe")
    driver.get(url)
    # time.sleep(50)
    # Определение конца загрузки сайта ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    try:
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='loader__bar --animation-finished']")))
    except Exception:
        print('Ошибка - страница загружена не полностью. Возможно входные данные недостоверны')
    else:
        print('ОК - Страница загрузилась полностью')
    # time.sleep(1)
    # Поиск цен по разному кол-ву пересадок ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    alt1 = ''
    src1 = ''
    alt2 = ''
    src2 = ''
    price_0_transfer = ''
    price_1_transfer = ''
    price_2_transfer = ''

    tt = driver.page_source
    price_0_transfer = "Не найдено"
    price_1_transfer = "Не найдено"
    price_2_transfer = "Не найдено"
    f = tt.split('class="checkboxes-list__extra-uncheck-other')
    if len(f) == 2:
        f1 = f[1].split('span class="price --rub">')
        price_0_transfer = f1[1].split("<")[0].replace('\u2009', '')
    if len(f) == 3:
        f1 = f[1].split('span class="price --rub">')
        f2 = f[2].split('span class="price --rub">')
        price_0_transfer = f1[1].split("<")[0].replace('\u2009', '')
        price_1_transfer = f2[1].split("<")[0].replace('\u2009', '')
    if len(f) > 3:
        f1 = f[1].split('span class="price --rub">')
        f2 = f[2].split('span class="price --rub">')
        f3 = f[3].split('span class="price --rub">')
        price_0_transfer = f1[1].split("<")[0].replace('\u2009', '')
        price_1_transfer = f2[1].split("<")[0].replace('\u2009', '')
        price_2_transfer = f3[1].split("<")[0].replace('\u2009', '')
    # Поиск самой дешевой цены ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    v = []
    lowest_price = ""
    xe = driver.find_element_by_xpath("//*[@class='product-list__item fade-enter-done']")
    xe2 = list(map(lambda x: x.replace('\u2009', ''), xe.text.split('\n')))
    try:
        lowest_price = str(xe2[xe2.index("Купить") + 1][3:])
    except ValueError:
        print('Ошибка - Не найдена самая низка цена из 10-ти запросов')
    # Поиск времени в пути ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    for i in xe2:
        if i.startswith('В пути'):
            v.append(i)
    if not v:
        v = ['-', '-']
        print('Ошибка - Не найдено время в пути')
    luggage = xe2[0]  # тут определяем багаж
    # Поиск названия авиакомпании и ссылки на картинку ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    try:
        xe4 = driver.find_elements_by_xpath(
            "//*[@class='product-list__item fade-enter-done'][1]//*[@class='ticket-carrier__img']")
    except ValueError:
        print('Ошибка - Не найдено название авиакомпании')
    else:
        attrs = []
        if len(xe4) == 1:
            for attr in xe4[0].get_property('attributes'):
                attrs.append([attr['name'], attr['value']])
                for i in range(len(attrs)):
                    if attrs[i][0] == 'src':
                        src1 = attrs[i][1][2:]
                    if attrs[i][0] == 'alt':
                        alt1 = attrs[i][1]
        else:
            for attr in xe4[0].get_property('attributes'):
                attrs.append([attr['name'], attr['value']])
                for i in range(len(attrs)):
                    if attrs[i][0] == 'src':
                        src1 = attrs[i][1][2:]
                    if attrs[i][0] == 'alt':
                        alt1 = attrs[i][1]
            for attr in xe4[1].get_property('attributes'):
                attrs.append([attr['name'], attr['value']])
                for i in range(len(attrs)):
                    if attrs[i][0] == 'src':
                        src2 = attrs[i][1][2:]
                    if attrs[i][0] == 'alt':
                        alt2 = attrs[i][1]
        print('ОК - Найдено авиакомпаний:', len(xe4))

        # print(attrs)
    rezult = ["Перелет без пересадок: " + price_0_transfer,
              "Перелет с 1-й пересадкой: " + price_1_transfer,
              "Перелет с 2-мя пересадками: " + price_2_transfer,
              "Самая низкая цена: " + lowest_price,
              "Багаж: " + luggage,
              "Туда " + v[0].lower(),
              "Обратно " + v[1].lower(),
              ]
    if alt2 != '':
        rezult += ["Авиакомпания 1: " + alt1, src1, "Авиакомпания 2: " + alt2, src2]
    else:
        rezult += ["Авиакомпания: " + alt1, src1]

    driver.quit()
    return rezult
