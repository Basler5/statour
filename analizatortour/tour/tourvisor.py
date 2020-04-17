import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import datetime

# DEMO_DATA
destination_country = ""
hotel_name = ""
date_of_departure = ""
return_date = ""
count_of_hotel_stars = ""
type_of_food = ""  # Питание: Завтрак = 2; Завтр+ужин = 3; Полный пансинон = 4; Все включено = 5;
hotel_rating = ""  # 3.0 и более = 2; 3.5 и более = 3; 4.0 и более = 4; 4.5 и более = 5;
number_of_adults = "0"  # number_of_adults / кол-во врослых от 12 лет
number_of_children = "0"  # number_of_children / кол-во детей от 2х до 12 лет

if int(number_of_children) > int(number_of_adults):
    number_of_children = number_of_adults
month_word = {
    1: "ЯНВАРЬ",
    2: "ФЕВРАЛЬ",
    3: "МАРТ",
    4: "АПРЕЛЬ",
    5: "МАЙ",
    6: "ИЮНЬ",
    7: "ИЮЛЬ",
    8: "АВГУСТ",
    9: "СЕНТЯБРЬ",
    10: "ОКТЯБРЬ",
    11: "НОЯБРЬ",
    12: "ДЕКАБРЬ",
}

def search_tourvisor(
    destination_country=destination_country,
    hotel_name=hotel_name.upper(),
    date_of_departure=date_of_departure,
    return_date=return_date,
    count_of_hotel_stars=count_of_hotel_stars,
    type_of_food=type_of_food,
    hotel_rating=hotel_rating,
    number_of_adults=number_of_adults,
    number_of_children=number_of_children,
            ):
    mon_of_dep = str(month_word.get(date_of_departure.month))
    day_of_dep = str(date_of_departure.day)
    duration_of_the_trip = (return_date - date_of_departure).days
    if hotel_name != "":
        hotel_name = hotel_name.upper()

    rez_hotel = ''
    rez_hotel_name = ''
    rating_location = ''
    rating_service = ''
    rating_food = ''
    rez_type_of_food = ''
    rez_type_of_room = ''
    stars = ''
    location = ''
    price_for_tour = ''
    # Инициализация запроса ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    url = 'https://tourvisor.ru/search.php'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/User/djangosite/tour/chromedriver.exe")
    driver.get(url)
    # time.sleep(20)
    # Определение конца загрузки сайта ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='TVSearchButton']")))
    except Exception:
        print('Ошибка - страница загружена не полностью. Возможно входные данные недостоверны')
    else:
        print('ОК - Страница загрузилась полностью')

    # print(driver.page_source)
    # Выбор страны ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    driver.find_element_by_xpath("//*[@class='TVMainFilterButton TVCountry']").click()
    driver.find_element_by_xpath("//*[@class='TVDropPanelBtn TVBtnAllCountry']").click()
    driver.find_element_by_xpath("//*[text()='" + destination_country + "']").click()
    # Выбор даты вылета ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    driver.find_element_by_xpath("//*[@class='TVMainFilterButton TVDates']").click()
    while driver.find_element_by_xpath("//*[@class='TVCalendarControlHeaderMonth']").text != mon_of_dep:
        driver.find_element_by_xpath("//*[@class='TVCalendarControlRightButton']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@data-value='" + day_of_dep + "']").click()
    driver.find_element_by_xpath("//*[@data-value='" + day_of_dep + "']").click()
    # Выбор кол-ва ночей ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    driver.find_element_by_xpath("//*[@class='TVMainFilterButton TVNights']").click()
    element = driver.find_element_by_xpath(
        "//*[@class='TVNightTableCells']//*[text()='" + str(duration_of_the_trip) + "']")
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    # Выбор кол-ва взрослых ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    if int(number_of_adults) != 2 or int(number_of_children) != 0:
        driver.find_element_by_xpath("//*[@class='TVMainFilterButton TVTourists']").click()
        if int(number_of_adults) < 2:
            driver.find_element_by_xpath(
                "//div[@class='TVTouristStatic']//div[@class='TVTouristContentMinus']").click()
        if int(number_of_adults) > 2:
            for i in range(int(number_of_adults) - 2):
                driver.find_element_by_xpath(
                    "//div[@class='TVTouristStatic']//div[@class='TVTouristContentPlus']").click()
    # Выбор кол-ва детей ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
        if int(number_of_children) != 0:
            for i in range(int(number_of_children)):
                driver.find_element_by_xpath(
                    "//div[@class='TVTouristsOptions']//div[@class='TVTouristElement TVTouristButton']").click()
                driver.find_element_by_xpath("//div[@class='TVSelectAgeTable']//div[text()='10 лет']").click()
        driver.find_element_by_xpath("//*[@class='TVMainFilterButton TVTourists']").click()
    # Если поле ОТЕЛЬ заполнено ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    if hotel_name != '':
        driver.find_element_by_xpath("//input[@placeholder='Введите название']").send_keys(hotel_name)
        time.sleep(2.5)
        kk = driver.find_element_by_xpath("//*[@class=' TVListBox TVStyleScroll']").text.split('\n')
        slov = {}
        mm = ''
        for i in kk:
            for j in range(min(len(i), len(hotel_name))):
                if i[j] == hotel_name[j]:
                    slov[i] = slov.get(i, 0) + 1
        for i in slov:
            if rez_hotel:
                if slov[s] > mm:
                    rez_hotel = i
                    mm = slov[i]
            else:
                rez_hotel = i
                mm = slov[i]
        driver.find_element_by_xpath("//div[text()='" + rez_hotel + "']").click()
    # Если поле ОТЕЛЬ не заполнено ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    else:
        # Выбор звезд отеля ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
        if int(count_of_hotel_stars):
            driver.find_element_by_xpath("//*[@class='TVOptionStars']/div[" + str(count_of_hotel_stars) + "]").click()
        # Выбор питания ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
        if int(type_of_food):
            driver.find_element_by_xpath(
                "//div[@class='TVOptionFilterBlock TVMeal']/div[@class='TVOptionSelector TVComboBox']").click()
            driver.find_element_by_xpath(
                "//div[@class='tv_content']/div[@class=' TVListBox TVStyleScroll']/div[" + str(type_of_food) + "]").click()
        # Выбор рейтинг ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
        if int(hotel_rating):
            driver.find_element_by_xpath(
                "//div[@class='TVOptionFilterBlock TVRating']/div[@class='TVOptionSelector TVComboBox']").click()
            driver.find_element_by_xpath(
                "//div[@class='tv_content']/div[@class=' TVListBox TVStyleScroll']/div[" + str(hotel_rating) + "]").click()

    # Запуск поиска ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    driver.find_element_by_xpath("//*[@class='TVSearchButton']").click()
    # Ожидание результата выдачи ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    try:
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='TVNewProgressBar TVHide']")))
    except Exception:
        print('Ошибка - поисковая выдача загружена не полностью. Возможно результат вывода будет недостоверным')
    else:
        print('ОК - Поисковая выдача загрузилась полностью')
        # Начало сбора данных до нажатия на вкладки ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
        rez_hotel_name = driver.find_element_by_xpath("//div[@class='blpricesort'][1]//div[@class='TVHotelName']").text
        location = driver.find_element_by_xpath("//div[@class='blpricesort'][1]//div[@class='TVRegion']").text
        stars = str(len(driver.find_elements_by_xpath("//div[@class='blpricesort'][1]//div[@class='TVStar']")))
        price_for_tour = driver.find_element_by_xpath(
            "//div[@class='blpricesort'][1]//div[@class='TVPriceValue']").text.replace(' ', '')
    # Сбор данных во вкладке Review ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    driver.find_element_by_xpath("//*[@class='TVNavButton TVReviewTitle']").click()
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='dynamics-l']")))
    except Exception:
        print('Ошибка - Вкладка с рейтингами не загружена')
    else:
        print('ОК - Вкладка с рейтингами загружена')
        rating = driver.find_element_by_xpath("//*[@class='dynamics-l']").text.split('\n')
        rating_location = rating[1] + " " + rating[2]
        rating_service = rating[3] + " " + rating[4]
        rating_food = rating[5] + " " + rating[6]
    # Сбор данных во вкладке Price ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    driver.find_element_by_xpath("//*[@class='TVNavButton TVPriceTitle']").click()
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='TVTem2PriceWrap']")))
    except Exception:
        print('Ошибка - Вкладки с ценами не загружена')
    else:
        print('ОК - Вкладка с ценами загружена')
        rez_type_of_food = driver.find_element_by_xpath(
            "//div[@class='TVTem2PriceContainer']/table/tbody/tr[2]/td[@class='TVTem2ThirdCol']/div[2]").text
        rez_type_of_room = driver.find_element_by_xpath(
            "//div[@class='TVTem2PriceContainer']/table/tbody/tr[2]/td[@class='TVTem2ThirdCol']"
            "/div[@class='TVTem2TopRow']/span[1]").text + " / " + driver.find_element_by_xpath(
            "//div[@class='TVTem2PriceContainer']/table/tbody/tr[2]"
            "/td[@class='TVTem2ThirdCol']/div[@class='TVTem2TopRow']/span[2]").text

    fff = driver.find_element_by_xpath("//*[2]/td[@class='TVTem2FirstCol' and 1]/img[1]").get_property('attributes')
    link_to_the_tour_operator = ''
    for attr in fff:
        link_to_the_tour_operator = attr['value']
    # Вывод результата ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
    rezult = ["Название отеля: " + rez_hotel_name,
              "Кол-во звезд отеля: " + stars,
              "Расположение отеля: " + location,
              "Рейтинги отеля: " + rating_location + "; " + rating_service + "; " + rating_food + ";",
              "Тип питания: " + rez_type_of_food,
              "Тип номера: " + rez_type_of_room,
              "Туроператор: " + link_to_the_tour_operator,
              "Цена за тур: " + price_for_tour,
              ]
    return rezult
