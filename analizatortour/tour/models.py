from django.db import models
from django.utils import timezone
import datetime


class SearchRequest(models.Model):
    var_for_departure_country = (
        ("RU", "Россия"),
        ("BY", "Беларусь"),
        ("KZ", "Казахстан"),
        ("ANY", "Другие страны"),
    )

    var_for_departure_city = (
        ("Любой", "Любой"),
        ("Абакан", "Абакан"),
        ("Анапа", "Анапа"),
        ("Архангельск", "Архангельск"),
        ("Астрахань", "Астрахань"),
        ("Барнаул", "Барнаул"),
        ("Белгород", "Белгород"),
        ("Благовещенск", "Благовещенск"),
        ("Братск", "Братск"),
        ("Брянск", "Брянск"),
        ("Владивосток", "Владивосток"),
        ("Владикавказ", "Владикавказ"),
        ("Волгоград", "Волгоград"),
        ("Воронеж", "Воронеж"),
        ("Грозный", "Грозный"),
        ("Екатеринбург", "Екатеринбург"),
        ("Иваново", "Иваново"),
        ("Ижевск", "Ижевск"),
        ("Иркутск", "Иркутск"),
        ("Казань", "Казань"),
        ("Калининград", "Калининград"),
        ("Калуга", "Калуга"),
        ("Кемерово", "Кемерово"),
        ("Киров", "Киров"),
        ("Краснодар", "Краснодар"),
        ("Красноярск", "Красноярск"),
        ("Курск", "Курск"),
        ("Липецк", "Липецк"),
        ("Магнитогорск", "Магнитогорск"),
        ("Махачкала", "Махачкала"),
        ("Мин.Воды", "Мин.Воды"),
        ("Москва", "Москва"),
        ("Мурманск", "Мурманск"),
        ("Н.Новгород", "Н.Новгород"),
        ("Наб.Челны", "Наб.Челны"),
        ("Нальчик", "Нальчик"),
        ("Нижневартовск", "Нижневартовск"),
        ("Нижнекамск", "Нижнекамск"),
        ("Новокузнецк", "Новокузнецк"),
        ("Новосибирск", "Новосибирск"),
        ("Новый Уренгой", "Новый Уренгой"),
        ("Омск", "Омск"),
        ("Оренбург", "Оренбург"),
        ("Орск", "Орск"),
        ("П.Камчатский", "П.Камчатский"),
        ("Пенза", "Пенза"),
        ("Пермь", "Пермь"),
        ("Ростов-на-Дону", "Ростов-на-Дону"),
        ("С.Петербург", "С.Петербург"),
        ("Самара", "Самара"),
        ("Саранск", "Саранск"),
        ("Саратов", "Саратов"),
        ("Симферополь", "Симферополь"),
        ("Сочи", "Сочи"),
        ("Ставрополь", "Ставрополь"),
        ("Сургут", "Сургут"),
        ("Сыктывкар", "Сыктывкар"),
        ("Томск", "Томск"),
        ("Тюмень", "Тюмень"),
        ("Улан-Удэ", "Улан-Удэ"),
        ("Ульяновск", "Ульяновск"),
        ("Уфа", "Уфа"),
        ("Хабаровск", "Хабаровск"),
        ("Ханты-Мансийск", "Ханты-Мансийск"),
        ("Чебоксары", "Чебоксары"),
        ("Челябинск", "Челябинск"),
        ("Череповец", "Череповец"),
        ("Чита", "Чита"),
        ("Ю.Сахалинск", "Ю.Сахалинск"),
        ("Якутск", "Якутск"),
        ("Ярославль", "Ярославль"),
        ("Брест", "Брест"),
        ("Витебск", "Витебск"),
        ("Гомель", "Гомель"),
        ("Гродно", "Гродно"),
        ("Минск", "Минск"),
        ("Могилев", "Могилев"),
        ("Актау", "Актау"),
        ("Актобе", "Актобе"),
        ("Алматы", "Алматы"),
        ("Атырау", "Атырау"),
        ("Караганды", "Караганды"),
        ("Костанай", "Костанай"),
        ("Кызылорда", "Кызылорда"),
        ("Нур-Султан", "Нур-Султан"),
        ("Павлодар", "Павлодар"),
        ("Петропавловск", "Петропавловск"),
        ("Тараз", "Тараз"),
        ("Уральск", "Уральск"),
        ("Усть-Каменогорск", "Усть-Каменогорск"),
        ("Шымкент", "Шымкент"),
        ("Баку", "Баку"),
        ("Бишкек", "Бишкек"),
        ("Варшава", "Варшава"),
        ("Вильнюс", "Вильнюс"),
        ("Винница", "Винница"),
        ("Днепр", "Днепр"),
        ("Запорожье", "Запорожье"),
        ("Ивано-Франковск", "Ивано-Франковск"),
        ("Каунас", "Каунас"),
        ("Киев", "Киев"),
        ("Кривой Рог", "Кривой Рог"),
        ("Львов", "Львов"),
        ("Николаев", "Николаев"),
        ("Одесса", "Одесса"),
        ("Рига", "Рига"),
        ("Таллин", "Таллин"),
        ("Ташкент", "Ташкент"),
        ("Харьков", "Харьков"),
        ("Херсон", "Херсон"),
        ("Черновцы", "Черновцы"),
    )

    var_for_changing_date = (
        ("var_day_0", "Без отклонения"),
        ("var_day_1", "1 день(+/-)"),
        ("var_day_2", "2 день(+/-)"),
        ("var_day_3", "3 день(+/-)"),
    )

    var_for_destination_country = (
        # ("Абхазия", "Абхазия"),
        # ("Австрия", "Австрия"),
        # ("Азербайджан", "Азербайджан"),
        # ("Албания", "Албания"),
        # ("Андорра", "Андорра"),
        # ("Армения", "Армения"),
        # ("Аруба", "Аруба"),
        # ("Багамы", "Багамы"),
        # ("Бахрейн", "Бахрейн"),
        # ("Беларусь", "Беларусь"),
        # ("Бельгия", "Бельгия"),
        # ("Болгария", "Болгария"),
        # ("Бразилия", "Бразилия"),
        # ("Великобритания", "Великобритания"),
        # ("Венгрия", "Венгрия"),
        # ("Вьетнам", "Вьетнам"),
        # ("Гамбия", "Гамбия"),
        # ("Германия", "Германия"),
        # ("Греция", "Греция"),
        # ("Грузия", "Грузия"),
        # ("Дания", "Дания"),
        # ("Доминикана", "Доминикана"),
        # ("Египет", "Египет"),
        # ("Израиль", "Израиль"),
        # ("Индия", "Индия"),
        # ("Индонезия", "Индонезия"),
        # ("Иордания", "Иордания"),
        # ("Ирландия", "Ирландия"),
        # ("Исландия", "Исландия"),
        # ("Испания", "Испания"),
        # ("Италия", "Италия"),
        # ("Казахстан", "Казахстан"),
        # ("Камбоджа", "Камбоджа"),
        # ("Катар", "Катар"),
        # ("Кения", "Кения"),
        # ("Кипр", "Кипр"),
        # ("Киргизия", "Киргизия"),
        # ("Китай", "Китай"),
        # ("Коста-Рика", "Коста-Рика"),
        # ("Куба", "Куба"),
        # ("Латвия", "Латвия"),
        # ("Ливан", "Ливан"),
        # ("Литва", "Литва"),
        # ("Маврикий", "Маврикий"),
        # ("Малайзия", "Малайзия"),
        # ("Мальдивы", "Мальдивы"),
        # ("Мальта", "Мальта"),
        # ("Марокко", "Марокко"),
        # ("Мексика", "Мексика"),
        # ("Мьянма", "Мьянма"),
        # ("Нидерланды", "Нидерланды"),
        # ("Норвегия", "Норвегия"),
        # ("ОАЭ", "ОАЭ"),
        # ("Оман", "Оман"),
        # ("Польша", "Польша"),
        # ("Португалия", "Португалия"),
        # ("Россия", "Россия"),
        # ("Румыния", "Румыния"),
        # ("Сейшелы", "Сейшелы"),
        # ("Сербия", "Сербия"),
        # ("Сингапур", "Сингапур"),
        # ("Словакия", "Словакия"),
        # ("Словения", "Словения"),
        # ("США", "США"),
         ("Таиланд", "Таиланд"),
        # ("Танзания", "Танзания"),
         ("Тунис", "Тунис"),
         ("Турция", "Турция"),
        # ("Узбекистан", "Узбекистан"),
         ("Филиппины", "Филиппины"),
        # ("Финляндия", "Финляндия"),
        # ("Франция", "Франция"),
        # ("Хорватия", "Хорватия"),
        # ("Черногория", "Черногория"),
        # ("Чехия", "Чехия"),
        # ("Швейцария", "Швейцария"),
        # ("Швеция", "Швеция"),
        # ("Шри-Ланка", "Шри-Ланка"),
        # ("Эстония", "Эстония"),
        # ("ЮАР", "ЮАР"),
        # ("Южная Корея", "Южная Корея"),
        # ("Ямайка", "Ямайка"),
         ("Япония", "Япония"),
    )

    var_for_destination_resort = (
        ("Новый", "Новый"),
        ("Гагра", "Гагра"),
        ("Гудаута", "Гудаута"),
        ("Новый Афон", "Новый Афон"),
        ("Пицунда", "Пицунда"),
        ("Сухум", "Сухум"),
        ("Бад Гаштайн", "Бад Гаштайн"),
        ("Бад Хофгаштайн", "Бад Хофгаштайн"),
        ("Баден", "Баден"),
        ("Бургенланд", "Бургенланд"),
        ("Вена", "Вена"),
        ("Верхняя Австрия", "Верхняя Австрия"),
        ("Заальбах-Хинтерглемм", "Заальбах-Хинтерглемм"),
        ("Зальцбург", "Зальцбург"),
        ("Зеефельд", "Зеефельд"),
        ("Зельден", "Зельден"),
        ("Инсбрук", "Инсбрук"),
        ("Ишгль", "Ишгль"),
        ("Капрун", "Капрун"),
        ("Каринтия", "Каринтия"),
        ("Китцбюэль-Кирхберг", "Китцбюэль-Кирхберг"),
        ("Лангенфельд", "Лангенфельд"),
        ("Лех", "Лех"),
        ("Лиенц", "Лиенц"),
        ("Майрхофен", "Майрхофен"),
        ("Нижняя Австрия", "Нижняя Австрия"),
        ("Нойштифт", "Нойштифт"),
        ("Обергургль-Хохгургль", "Обергургль-Хохгургль"),
        ("Серфаус", "Серфаус"),
        ("Ст. Антон", "Ст. Антон"),
        ("Хинтертукс", "Хинтертукс"),
        ("Хиппах", "Хиппах"),
        ("Цель ам Зее", "Цель ам Зее"),
        ("Цель ам Циллер", "Цель ам Циллер"),
        ("Штирия", "Штирия"),
        ("Баку", "Баку"),
        ("Габала", "Габала"),
        ("Нафталан", "Нафталан"),
        ("Шахдаг", "Шахдаг"),
        ("Шеки", "Шеки"),
        ("Влера", "Влера"),
        ("Дуррес", "Дуррес"),
        ("Ксамиль", "Ксамиль"),
        ("Саранда", "Саранда"),
        ("Тирана", "Тирана"),
        ("Андорра ла Велла", "Андорра ла Велла"),
        ("Канильо", "Канильо"),
        ("Ла Массана", "Ла Массана"),
        ("Ордино-Аркалис", "Ордино-Аркалис"),
        ("Пал-Аринсал", "Пал-Аринсал"),
        ("Пас де ла Касса", "Пас де ла Касса"),
        ("Сольдеу", "Сольдеу"),
        ("Энкамп", "Энкамп"),
        ("Эскальдес", "Эскальдес"),
        ("Джермук", "Джермук"),
        ("Ереван", "Ереван"),
        ("Лори", "Лори"),
        ("Севан", "Севан"),
        ("Цахкадзор", "Цахкадзор"),
        ("Аруба", "Аруба"),
        ("Багамы", "Багамы"),
        ("Манама", "Манама"),
        ("Антверпен", "Антверпен"),
        ("Брюгге", "Брюгге"),
        ("Брюссель", "Брюссель"),
        ("Гент", "Гент"),
        ("Албена", "Албена"),
        ("Бургас", "Бургас"),
        ("Варна", "Варна"),
        ("Велико-Тырново", "Велико-Тырново"),
        ("Горн.лыжи", "Горн.лыжи"),
        ("Золотые Пески", "Золотые Пески"),
        ("Обзор", "Обзор"),
        ("Солнечный Берег", "Солнечный Берег"),
        ("София", "София"),
        ("Ангра дус Рейс", "Ангра дус Рейс"),
        ("Белен", "Белен"),
        ("Бразилиа", "Бразилиа"),
        ("Бузиос", "Бузиос"),
        ("Игуасу", "Игуасу"),
        ("Кампу Гранди", "Кампу Гранди"),
        ("Куритиба", "Куритиба"),
        ("Манаус", "Манаус"),
        ("Минас Жерайс", "Минас Жерайс"),
        ("Натал", "Натал"),
        ("Порту Алегри", "Порту Алегри"),
        ("Ресифе", "Ресифе"),
        ("Рио де Жанейро", "Рио де Жанейро"),
        ("Сальвадор", "Сальвадор"),
        ("Сан Паулу", "Сан Паулу"),
        ("Санта Катарина", "Санта Катарина"),
        ("Сеара", "Сеара"),
        ("Лондон", "Лондон"),
        ("Эдинбург", "Эдинбург"),
        ("Балатон", "Балатон"),
        ("Будапешт", "Будапешт"),
        ("Бюк", "Бюк"),
        ("Дебрецен", "Дебрецен"),
        ("Мишкольц", "Мишкольц"),
        ("Хайдусобосло", "Хайдусобосло"),
        ("Хевиз", "Хевиз"),
        ("Шарвар", "Шарвар"),
        ("Шопрон", "Шопрон"),
        ("Эгер", "Эгер"),
        ("Юж.Задунайский кр.", "Юж.Задунайский кр."),
        ("Вунг Тау", "Вунг Тау"),
        ("Дананг", "Дананг"),
        ("Нячанг", "Нячанг"),
        ("Пхан Ранг", "Пхан Ранг"),
        ("Фантьет", "Фантьет"),
        ("Фукуок", "Фукуок"),
        ("Ханой", "Ханой"),
        ("Хой Ан", "Хой Ан"),
        ("Хошимин", "Хошимин"),
        ("Банжул", "Банжул"),
        ("Бавария", "Бавария"),
        ("Баден Вюртемберг", "Баден Вюртемберг"),
        ("Берлин", "Берлин"),
        ("Бремен", "Бремен"),
        ("Гамбург", "Гамбург"),
        ("Дрезден", "Дрезден"),
        ("Дюссельдорф", "Дюссельдорф"),
        ("Кельн", "Кельн"),
        ("Мюнхен", "Мюнхен"),
        ("Озера Германии", "Озера Германии"),
        ("Рейнланд Пфальц", "Рейнланд Пфальц"),
        ("Франкфурт", "Франкфурт"),
        ("Шлезвиг Гольштейн", "Шлезвиг Гольштейн"),
        ("Афины", "Афины"),
        ("Дельфы", "Дельфы"),
        ("Закинф", "Закинф"),
        ("Кавала", "Кавала"),
        ("Касторья", "Касторья"),
        ("Кефалония", "Кефалония"),
        ("Киклады", "Киклады"),
        ("Корфу", "Корфу"),
        ("Кос", "Кос"),
        ("Крит - Ираклион", "Крит - Ираклион"),
        ("Крит - Лассити", "Крит - Лассити"),
        ("Крит - Ретимно", "Крит - Ретимно"),
        ("Крит - Ханья", "Крит - Ханья"),
        ("Пелопоннес", "Пелопоннес"),
        ("Пиерия", "Пиерия"),
        ("Родос", "Родос"),
        ("Салоники", "Салоники"),
        ("Самос", "Самос"),
        ("Санторини", "Санторини"),
        ("Скиатос", "Скиатос"),
        ("Тасос", "Тасос"),
        ("Фессалия", "Фессалия"),
        ("Халкидики", "Халкидики"),
        ("Хиос", "Хиос"),
        ("Эвия", "Эвия"),
        ("Эвритания", "Эвритания"),
        ("Бакуриани", "Бакуриани"),
        ("Батуми", "Батуми"),
        ("Боржоми", "Боржоми"),
        ("Гудаури", "Гудаури"),
        ("Кахетия", "Кахетия"),
        ("Кобулети", "Кобулети"),
        ("Кутаиси", "Кутаиси"),
        ("Сванетия", "Сванетия"),
        ("Тбилиси", "Тбилиси"),
        ("Уреки", "Уреки"),
        ("Биллунд", "Биллунд"),
        ("Копенгаген", "Копенгаген"),
        ("Бока Чика", "Бока Чика"),
        ("Ла Романа", "Ла Романа"),
        ("Пунта Кана", "Пунта Кана"),
        ("Пуэрто Плата", "Пуэрто Плата"),
        ("Хуан Долио", "Хуан Долио"),
        ("Дахаб", "Дахаб"),
        ("Каир", "Каир"),
        ("Марса Алам", "Марса Алам"),
        ("Нувейба", "Нувейба"),
        ("Сафага", "Сафага"),
        ("Таба", "Таба"),
        ("Хургада", "Хургада"),
        ("Шарм-Эль-Шейх", "Шарм-Эль-Шейх"),
        ("Эль Гуна", "Эль Гуна"),
        ("Герцлия", "Герцлия"),
        ("Иерусалим", "Иерусалим"),
        ("Мертвое море", "Мертвое море"),
        ("Нетания", "Нетания"),
        ("Тверия", "Тверия"),
        ("Тель-Авив", "Тель-Авив"),
        ("Хайфа", "Хайфа"),
        ("Эйлат", "Эйлат"),
        ("Керала", "Керала"),
        ("Нью Дели", "Нью Дели"),
        ("Север Гоа", "Север Гоа"),
        ("Центр Гоа", "Центр Гоа"),
        ("Юг Гоа", "Юг Гоа"),
        ("Бали", "Бали"),
        ("Бинтан", "Бинтан"),
        ("Ломбок", "Ломбок"),
        ("Акаба", "Акаба"),
        ("Амман", "Амман"),
        ("Мертвое море", "Мертвое море"),
        ("Петра", "Петра"),
        ("Дублин", "Дублин"),
        ("Рейкьявик", "Рейкьявик"),
        ("Альмерия", "Альмерия"),
        ("Барселона", "Барселона"),
        ("Валенсия", "Валенсия"),
        ("Горные лыжи", "Горные лыжи"),
        ("Гран Канария", "Гран Канария"),
        ("Ибица", "Ибица"),
        ("Коста Бланка", "Коста Бланка"),
        ("Коста Брава", "Коста Брава"),
        ("Коста де ла Луз", "Коста де ла Луз"),
        ("Коста Дель Маресме", "Коста Дель Маресме"),
        ("Коста Дель Соль", "Коста Дель Соль"),
        ("Коста Дорада", "Коста Дорада"),
        ("Коста Тропикаль", "Коста Тропикаль"),
        ("Лансароте", "Лансароте"),
        ("Мадрид", "Мадрид"),
        ("Майорка", "Майорка"),
        ("Менорка", "Менорка"),
        ("Мурсия", "Мурсия"),
        ("Севилья", "Севилья"),
        ("Страна Басков", "Страна Басков"),
        ("Тенерифе", "Тенерифе"),
        ("Фуэртевентура", "Фуэртевентура"),
        ("Абруццо", "Абруццо"),
        ("Апулия", "Апулия"),
        ("Бибионе", "Бибионе"),
        ("Бормио", "Бормио"),
        ("Валле-д Аоста", "Валле-д Аоста"),
        ("Валь Гардена", "Валь Гардена"),
        ("Валь ди Суза", "Валь ди Суза"),
        ("Валь ди Фасса", "Валь ди Фасса"),
        ("Валь ди Фьемме", "Валь ди Фьемме"),
        ("Венето", "Венето"),
        ("Венецианская ривьера", "Венецианская ривьера"),
        ("Венеция", "Венеция"),
        ("Верона", "Верона"),
        ("Доломитовые Альпы", "Доломитовые Альпы"),
        ("Искья", "Искья"),
        ("Калабрия", "Калабрия"),
        ("Капри", "Капри"),
        ("Кортина д Ампеццо", "Кортина д Ампеццо"),
        ("Кронплатц", "Кронплатц"),
        ("Ливиньо", "Ливиньо"),
        ("Лигурия", "Лигурия"),
        ("Линьяно", "Линьяно"),
        ("Мадонна ди Кампильо", "Мадонна ди Кампильо"),
        ("Марке", "Марке"),
        ("Милан", "Милан"),
        ("Неаполитанский залив", "Неаполитанский залив"),
        ("Озера", "Озера"),
        ("Пассо Тонале", "Пассо Тонале"),
        ("Ривьера-ди-Улиссе", "Ривьера-ди-Улиссе"),
        ("Рим", "Рим"),
        ("Римини", "Римини"),
        ("Сан Мартино", "Сан Мартино"),
        ("Сардиния", "Сардиния"),
        ("Сицилия", "Сицилия"),
        ("Термальные курорты", "Термальные курорты"),
        ("Тоскана", "Тоскана"),
        ("Умбрия", "Умбрия"),
        ("Флоренция", "Флоренция"),
        ("Эльба", "Эльба"),
        ("Эмилия-Романья", "Эмилия-Романья"),
        ("Алматы", "Алматы"),
        ("Астана", "Астана"),
        ("Боровое", "Боровое"),
        ("Пномпень", "Пномпень"),
        ("Сиануквиль", "Сиануквиль"),
        ("Сием Рип", "Сием Рип"),
        ("Доха", "Доха"),
        ("Ватаму", "Ватаму"),
        ("Ламу", "Ламу"),
        ("Момбаса", "Момбаса"),
        ("Найроби", "Найроби"),
        ("Айя Напа", "Айя Напа"),
        ("Ларнака", "Ларнака"),
        ("Лимассол", "Лимассол"),
        ("Никосия", "Никосия"),
        ("Пафос", "Пафос"),
        ("Протарас", "Протарас"),
        ("Иссык-Куль", "Иссык-Куль"),
        ("Каракол", "Каракол"),
        ("Бэйдайхэ", "Бэйдайхэ"),
        ("Гонконг", "Гонконг"),
        ("Гуанчжоу", "Гуанчжоу"),
        ("Ляонин", "Ляонин"),
        ("Пекин", "Пекин"),
        ("Урумчи", "Урумчи"),
        ("Хайнань", "Хайнань"),
        ("Шанхай", "Шанхай"),
        ("Гуанакасте", "Гуанакасте"),
        ("Пунтаренас", "Пунтаренас"),
        ("Сан-Хосе", "Сан-Хосе"),
        ("Варадеро", "Варадеро"),
        ("Гавана", "Гавана"),
        ("Гуантанамо", "Гуантанамо"),
        ("Камагуэй", "Камагуэй"),
        ("Лос-Канарреос", "Лос-Канарреос"),
        ("Ольгин", "Ольгин"),
        ("Пинар-дель-Рио", "Пинар-дель-Рио"),
        ("Сантьяго-де-Куба", "Сантьяго-де-Куба"),
        ("Тринидад", "Тринидад"),
        ("Хардинес-дель-Рей", "Хардинес-дель-Рей"),
        ("Рига", "Рига"),
        ("Юрмала", "Юрмала"),
        ("Бейрут", "Бейрут"),
        ("Джуния", "Джуния"),
        ("Вильнюс", "Вильнюс"),
        ("Друскининкай", "Друскининкай"),
        ("Каунас", "Каунас"),
        ("Клайпеда", "Клайпеда"),
        ("Паланга", "Паланга"),
        ("Маврикий", "Маврикий"),
        ("Калимантан", "Калимантан"),
        ("Куала Лумпур", "Куала Лумпур"),
        ("Лангкави", "Лангкави"),
        ("Пангкор", "Пангкор"),
        ("Пенанг", "Пенанг"),
        ("Реданг", "Реданг"),
        ("Тиоман", "Тиоман"),
        ("Мальдивы", "Мальдивы"),
        ("Аттард", "Аттард"),
        ("Бирзеббуджа", "Бирзеббуджа"),
        ("Валлетта", "Валлетта"),
        ("Гозо", "Гозо"),
        ("Комино", "Комино"),
        ("Мдина", "Мдина"),
        ("Меллиха", "Меллиха"),
        ("Сент Джулианс", "Сент Джулианс"),
        ("Сент Полс Бэй", "Сент Полс Бэй"),
        ("Слима", "Слима"),
        ("Агадир", "Агадир"),
        ("Касабланка", "Касабланка"),
        ("Марракеш", "Марракеш"),
        ("Рабат", "Рабат"),
        ("Танжер", "Танжер"),
        ("Уарзазат", "Уарзазат"),
        ("Уджда", "Уджда"),
        ("Фес", "Фес"),
        ("Эль-Джадида", "Эль-Джадида"),
        ("Эрфуд", "Эрфуд"),
        ("Эссуэйра", "Эссуэйра"),
        ("Канкун", "Канкун"),
        ("Косумель", "Косумель"),
        ("Лос Кабос", "Лос Кабос"),
        ("Мехико", "Мехико"),
        ("Плайя Дель Кармен", "Плайя Дель Кармен"),
        ("Ривьера Майя", "Ривьера Майя"),
        ("Баган", "Баган"),
        ("Нгапали", "Нгапали"),
        ("Нгве Саунг", "Нгве Саунг"),
        ("Озеро Инле", "Озеро Инле"),
        ("Янгон", "Янгон"),
        ("Амстердам", "Амстердам"),
        ("Гаага", "Гаага"),
        ("Берген", "Берген"),
        ("Олесунн", "Олесунн"),
        ("Осло", "Осло"),
        ("Северная Норвегия", "Северная Норвегия"),
        ("Тронхейм", "Тронхейм"),
        ("Абу-Даби", "Абу-Даби"),
        ("Аджман", "Аджман"),
        ("Дубай", "Дубай"),
        ("Рас-эль-Хайм", "Рас-эль-Хайм"),
        ("Умм Аль Кувейн", "Умм Аль Кувейн"),
        ("Фуджейра", "Фуджейра"),
        ("Шарджа", "Шарджа"),
        ("Маскат", "Маскат"),
        ("Салала", "Салала"),
        ("Варшава", "Варшава"),
        ("Вроцлав", "Вроцлав"),
        ("Закопане", "Закопане"),
        ("Краков", "Краков"),
        ("Лечебные курорты", "Лечебные курорты"),
        ("Тройгород", "Тройгород"),
        ("Азорские острова", "Азорские острова"),
        ("Алгарве", "Алгарве"),
        ("Лиссабон", "Лиссабон"),
        ("Мадейра", "Мадейра"),
        ("Порту", "Порту"),
        ("Абзаково / Банное", "Абзаково / Банное"),
        ("Азовское море", "Азовское море"),
        ("Алтай", "Алтай"),
        ("Анапа", "Анапа"),
        ("Архыз", "Архыз"),
        ("Байкал", "Байкал"),
        ("Великий Устюг", "Великий Устюг"),
        ("Воронеж", "Воронеж"),
        ("Геленджик", "Геленджик"),
        ("Домбай", "Домбай"),
        ("Золотое Кольцо", "Золотое Кольцо"),
        ("Кав. Мин. Воды", "Кав. Мин. Воды"),
        ("Казань", "Казань"),
        ("Калининградская обл.", "Калининградская обл."),
        ("Карелия", "Карелия"),
        ("Красная поляна", "Красная поляна"),
        ("Крым", "Крым"),
        ("Москва/Подмосковье", "Москва/Подмосковье"),
        ("Новгородская обл.", "Новгородская обл."),
        ("Новосибирская обл.", "Новосибирская обл."),
        ("Приэльбрусье", "Приэльбрусье"),
        ("Псков", "Псков"),
        ("Ростов-на-Дону", "Ростов-на-Дону"),
        ("Самарская обл.", "Самарская обл."),
        ("Санкт-Петербург", "Санкт-Петербург"),
        ("Сочи", "Сочи"),
        ("Татарстан", "Татарстан"),
        ("Туапсе", "Туапсе"),
        ("Урал", "Урал"),
        ("Шерегеш", "Шерегеш"),
        ("Бухарест", "Бухарест"),
        ("Констанца", "Констанца"),
        ("Мамая", "Мамая"),
        ("Мангалия", "Мангалия"),
        ("Эфорие", "Эфорие"),
        ("Сейшелы", "Сейшелы"),
        ("Белград", "Белград"),
        ("Борский округ", "Борский округ"),
        ("Велико-Градиште", "Велико-Градиште"),
        ("Горн.лыжи", "Горн.лыжи"),
        ("Златибор", "Златибор"),
        ("Суботица", "Суботица"),
        ("Термальные курорты", "Термальные курорты"),
        ("Сентоза", "Сентоза"),
        ("Сингапур", "Сингапур"),
        ("Бардеевские Купели", "Бардеевские Купели"),
        ("Братислава", "Братислава"),
        ("Высокие Татры", "Высокие Татры"),
        ("Дудинце", "Дудинце"),
        ("Низкие Татры", "Низкие Татры"),
        ("Пиештяны", "Пиештяны"),
        ("Раецке Теплице", "Раецке Теплице"),
        ("Смрдаки", "Смрдаки"),
        ("Тренчьянске Теплице", "Тренчьянске Теплице"),
        ("Турчанске Теплице", "Турчанске Теплице"),
        ("Адриатика", "Адриатика"),
        ("Добрна", "Добрна"),
        ("Доленске Топлице", "Доленске Топлице"),
        ("Лашко", "Лашко"),
        ("Любляна", "Любляна"),
        ("Моравске Топлице", "Моравске Топлице"),
        ("Озера", "Озера"),
        ("Римске Топлице", "Римске Топлице"),
        ("Рогашка Слатина", "Рогашка Слатина"),
        ("Терме Олимия", "Терме Олимия"),
        ("Терме Раденци", "Терме Раденци"),
        ("Терме Чатеж", "Терме Чатеж"),
        ("Шмарьешке Топлице", "Шмарьешке Топлице"),
        ("Юлийские Альпы", "Юлийские Альпы"),
        ("Вашингтон", "Вашингтон"),
        ("Гавайи", "Гавайи"),
        ("Горные лыжи", "Горные лыжи"),
        ("Гуам", "Гуам"),
        ("Лас-Вегас", "Лас-Вегас"),
        ("Лос-Анджелес", "Лос-Анджелес"),
        ("Майами", "Майами"),
        ("Нью-Йорк", "Нью-Йорк"),
        ("Сайпан", "Сайпан"),
        ("Чикаго", "Чикаго"),
        ("Бангкок", "Бангкок"),
        ("Као Лак", "Као Лак"),
        ("Ко Чанг", "Ко Чанг"),
        ("Краби", "Краби"),
        ("Паттайя", "Паттайя"),
        ("Пхукет", "Пхукет"),
        ("Районг", "Районг"),
        ("Самуи", "Самуи"),
        ("Хуа Хин", "Хуа Хин"),
        ("Чианг Май", "Чианг Май"),
        ("Дар эс Салам", "Дар эс Салам"),
        ("Занзибар", "Занзибар"),
        ("Гаммарт", "Гаммарт"),
        ("Джерба", "Джерба"),
        ("Махдия", "Махдия"),
        ("Монастир", "Монастир"),
        ("Сусс", "Сусс"),
        ("Табарка", "Табарка"),
        ("Хаммамет", "Хаммамет"),
        ("Алания", "Алания"),
        ("Анталия", "Анталия"),
        ("Белек", "Белек"),
        ("Бодрум", "Бодрум"),
        ("Даламан", "Даламан"),
        ("Дидим", "Дидим"),
        ("Измир", "Измир"),
        ("Кайсери", "Кайсери"),
        ("Каппадокия", "Каппадокия"),
        ("Кемер", "Кемер"),
        ("Кушадасы", "Кушадасы"),
        ("Мармарис", "Мармарис"),
        ("Сиде", "Сиде"),
        ("Стамбул", "Стамбул"),
        ("Улудаг", "Улудаг"),
        ("Фетхие", "Фетхие"),
        ("Чешме", "Чешме"),
        ("Эрзурум", "Эрзурум"),
        ("Бухара", "Бухара"),
        ("Самарканд", "Самарканд"),
        ("Ташкент", "Ташкент"),
        ("Хива", "Хива"),
        ("Боракай", "Боракай"),
        ("Бохоль", "Бохоль"),
        ("Лусон", "Лусон"),
        ("Палаван", "Палаван"),
        ("Себу", "Себу"),
        ("Восточная Финляндия", "Восточная Финляндия"),
        ("Западная Финляндия", "Западная Финляндия"),
        ("Лапландия", "Лапландия"),
        ("Оулу", "Оулу"),
        ("Хельсинки", "Хельсинки"),
        ("Южная Финляндия", "Южная Финляндия"),
        ("Аквитания", "Аквитания"),
        ("Земли Луары", "Земли Луары"),
        ("Корсика", "Корсика"),
        ("Лазурный берег", "Лазурный берег"),
        ("Лангедок Руссильон", "Лангедок Руссильон"),
        ("Нор Па де Кале", "Нор Па де Кале"),
        ("Нормандия", "Нормандия"),
        ("Парадиски", "Парадиски"),
        ("Париж", "Париж"),
        ("Пиренеи", "Пиренеи"),
        ("Порт дю Солей", "Порт дю Солей"),
        ("Пуату Шаранта", "Пуату Шаранта"),
        ("Рона Альпы", "Рона Альпы"),
        ("Савойя", "Савойя"),
        ("Три Долины", "Три Долины"),
        ("Эльзас", "Эльзас"),
        ("Эспас Килли", "Эспас Килли"),
        ("Загреб", "Загреб"),
        ("Истрия", "Истрия"),
        ("Северная Далмация", "Северная Далмация"),
        ("Средняя Далмация", "Средняя Далмация"),
        ("Южная Далмация", "Южная Далмация"),
        ("Бар", "Бар"),
        ("Бечичи", "Бечичи"),
        ("Будва", "Будва"),
        ("Герцег Нови", "Герцег Нови"),
        ("Горн. лыжи", "Горн. лыжи"),
        ("Котор", "Котор"),
        ("Петровац", "Петровац"),
        ("Подгорица", "Подгорица"),
        ("Святой Стефан", "Святой Стефан"),
        ("Тиват", "Тиват"),
        ("Ульцин", "Ульцин"),
        ("Дарков", "Дарков"),
        ("Карловы Вары", "Карловы Вары"),
        ("Крконоше", "Крконоше"),
        ("Лазне Белоград", "Лазне Белоград"),
        ("Марианские Лазне", "Марианские Лазне"),
        ("Подебрады", "Подебрады"),
        ("Прага", "Прага"),
        ("Теплице", "Теплице"),
        ("Франтишкови Лазне", "Франтишкови Лазне"),
        ("Яхимов", "Яхимов"),
        ("Бад Рагац", "Бад Рагац"),
        ("Берн", "Берн"),
        ("Вале", "Вале"),
        ("Граубюнден", "Граубюнден"),
        ("Женева", "Женева"),
        ("Женевское озеро", "Женевское озеро"),
        ("Люцернское озеро", "Люцернское озеро"),
        ("Цюрих", "Цюрих"),
        ("Стокгольм", "Стокгольм"),
        ("Аругам Бей", "Аругам Бей"),
        ("Бентота", "Бентота"),
        ("Галле", "Галле"),
        ("Калутара", "Калутара"),
        ("Канди", "Канди"),
        ("Коггала", "Коггала"),
        ("Коломбо", "Коломбо"),
        ("Негомбо", "Негомбо"),
        ("Сигирия", "Сигирия"),
        ("Тангалле", "Тангалле"),
        ("Тринкомали", "Тринкомали"),
        ("Унаватуна", "Унаватуна"),
        ("Хиккадува", "Хиккадува"),
        ("Вирумаа", "Вирумаа"),
        ("Пярну", "Пярну"),
        ("Сааремаа", "Сааремаа"),
        ("Таллин", "Таллин"),
        ("Тарту", "Тарту"),
        ("Хаапсалу", "Хаапсалу"),
        ("Дурбан", "Дурбан"),
        ("Кейптаун", "Кейптаун"),
        ("Пусан", "Пусан"),
        ("Сеул", "Сеул"),
        ("Чеджу", "Чеджу"),
        ("Вестморлэнд", "Вестморлэнд"),
        ("Кингстон", "Кингстон"),
        ("Монтего Бэй", "Монтего Бэй"),
        ("Очо Риос", "Очо Риос"),
        ("Порт Антонио", "Порт Антонио"),
        ("Раневей Бэй", "Раневей Бэй"),
        ("Южное побережье", "Южное побережье"),
        ("Киото", "Киото"),
        ("Окинава", "Окинава"),
        ("Осака", "Осака"),
        ("Токио", "Токио"),

        # список из ~1000 (?) курортов который будет подсталяться при вводе в CharField с фильтрацией по странам
        # ошибка в случае, если такой курорт не найден
    )

    var_for_count_of_hotel_stars = (
        ("0", "Не важно"),
        ("2", "2 звезды"),
        ("3", "3 звезды"),
        ("4", "4 звезды"),
        ("5", "5 звезд"),
    )

    var_for_hotel_rating = (
        ("0", "Не важно"),
        ("5", "5 и более"),
        ("6", "6 и более"),
        ("7", "7 и более"),
        ("8", "8 и более"),
        ("9", "9 и более"),
    )

    var_for_type_of_food = (
        ("0", "Не важно"),
        ("2", "BB - Только завтрак"),
        ("3", "HB - Завтрак и ужин"),
        ("4", "FB - трех разовое питание"),
        ("5", "AL - Все включено"),
    )

    var_for_number_of_adults = (
        ("1", "1 взрослый"),
        ("2", "2 взрослых"),
        ("3", "3 взрослых"),
        ("4", "4 взрослых"),
        ("5", "5 взрослых"),
        ("6", "6 взрослых"),
    )

    var_for_number_of_children = (
        ("0", "Без детей"),
        ("1", "1 ребенок"),
        ("2", "2 ребенка"),
        ("3", "3 ребенка"),
        ("4", "4 ребенка"),
    )

    var_for_number_of_infants = (
        ("0", "Без грудных детей"),
        ("1", "1 грудной ребенок"),
        ("2", "2 грудных ребенка"),
        ("3", "3 грудных ребенка"),
    )

    """
    departure_country = forms.ChoiceField(choices=var_for_departure_country, label="Страна отправления",
        label_suffix="", widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    departure_city = forms.ChoiceField(choices=var_for_departure_city, label="Город отправления", label_suffix="",
        widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    date_of_departure = forms.DateField(label="Выбери дату начала путешествия", label_suffix="",
        initial=datetime.date.today() + datetime.timedelta(days=10), input_formats=['%Y-%m-%d'],
        widget=forms.TextInput(attrs={'type': 'date',
                                      'class': 'form-control',
                                      'min': datetime.date.today(),
                                      'max': datetime.date.today() + datetime.timedelta(days=365)}))
    changing_the_departure_date = forms.ChoiceField(choices=var_for_changing_date,
        label="Возможное отклонение даты начала", label_suffix="",
        widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    destination_country = forms.ChoiceField(choices=var_for_destination_country, initial="Таиланд", label="Страна назначения",
        label_suffix="", widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    destination_resort = forms.ChoiceField(choices=var_for_destination_resort, initial="Любой", label="Курорт назначения",
        label_suffix="", widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    hotel_name = forms.CharField(label="Отель", max_length=37, label_suffix="", required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'укажи отель'}))
    count_of_hotel_stars = forms.ChoiceField(choices=var_for_count_of_hotel_stars, label="Кол-во звезд отеля",
        label_suffix="", widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    hotel_rating = forms.ChoiceField(choices=var_for_hotel_rating, label="Рейтинг отеля",
        label_suffix="", widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    type_of_food = forms.ChoiceField(choices=var_for_type_of_food, label="Питание",
        label_suffix="", widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    return_date = forms.DateField(label="Выбери дату возвращения", label_suffix="",
        initial=datetime.date.today() + datetime.timedelta(days=24),
        input_formats=['%Y-%m-%d'],
        widget=forms.TextInput(attrs={'type': 'date',
                                      'class': 'form-control',
                                      'min': datetime.date.today() + datetime.timedelta(days=3),
                                      'max': datetime.date.today() + datetime.timedelta(days=365)}))
    changing_return_date = forms.ChoiceField(choices=var_for_changing_date,
        label="Возможное отклонение даты возвращения", label_suffix="",
        widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    number_of_adults = forms.ChoiceField(choices=var_for_number_of_adults,
        label="Кол-во взрослых", label_suffix="", initial="2",
        widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    number_of_children = forms.ChoiceField(choices=var_for_number_of_children,
        label="Кол-во детей до 12 лет", label_suffix="",
        widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    number_of_infants = forms.ChoiceField(choices=var_for_number_of_infants,
        label="Кол-во грудных детей до 2-х лет", label_suffix="",
        widget=forms.Select(attrs={'class': 'custom-select d-block w-100'}))
    direct_flights_only = forms.BooleanField(label="Только прямые рейсы", label_suffix="", required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'}))
    accommodation_at_the_hotel_only = forms.BooleanField(label_suffix="", required=False,
        label="Искаль только отели (исключить апартаменты/гостевые дома/санатории/виллы и т.д.)",
        widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'}))
    """

    date_time_request = models.DateTimeField(auto_now_add=datetime.datetime)

    departure_country = models.CharField(verbose_name="Страна отправления", max_length=3, choices=var_for_departure_country, default='RU')
    departure_city = models.CharField(verbose_name="Город отправления", max_length=60, choices=var_for_departure_city, default="Любой")
    date_of_departure = models.DateField(verbose_name="Выбери дату начала путешествия")
    changing_the_departure_date = models.CharField(verbose_name="Возможное отклонение даты начала", max_length=15, choices=var_for_changing_date, default="0")
    destination_country = models.CharField(verbose_name="Страна назначения", max_length=20, choices=var_for_destination_country, default="Таиланд")
    destination_resort = models.CharField(verbose_name="Курорт назначения", max_length=60, choices=var_for_destination_resort, default="Любой")
    hotel_name = models.CharField(verbose_name="Отель", max_length=40, blank=True, null=True)
    count_of_hotel_stars = models.CharField(verbose_name="Кол-во звезд отеля", max_length=1, choices=var_for_count_of_hotel_stars, default="0")
    hotel_rating = models.CharField(verbose_name="Рейтинг отеля", max_length=1, choices=var_for_hotel_rating, default="0")
    type_of_food = models.CharField(verbose_name="Питание", max_length=1, choices=var_for_type_of_food, default="0")
    return_date = models.DateField(verbose_name="Выбери дату возвращения")
    changing_return_date = models.CharField(verbose_name="Возможное отклонение даты возвращения", max_length=15, choices=var_for_changing_date, default="0")
    number_of_adults = models.CharField(verbose_name="Кол-во взрослых", max_length=1, choices=var_for_number_of_adults, default="2")
    number_of_children = models.CharField(verbose_name="Кол-во детей до 12 лет", max_length=1, choices=var_for_number_of_children, default="0")
    number_of_infants = models.CharField(verbose_name="Кол-во грудных детей до 2-х лет", max_length=1, choices=var_for_number_of_infants, default="0")
    direct_flights_only = models.BooleanField(verbose_name="Только прямые рейсы")
    accommodation_at_the_hotel_only = models.BooleanField(verbose_name="Искаль только отели (исключить апартаменты/гостевые дома/санатории/виллы и т.д.)")
    is_loading_ended = models.BooleanField(default=False)
    is_loading_failed = models.BooleanField(default=False)


    def __str__(self):
        return 'ID: {0}; Курорт: {1}; дата поиска: {2}'.format(
            self.pk, self.destination_resort, self.date_time_request.date())


'''
    def publish(self):
        self.point_of_departure = MOW
        self.save()
'''


# user_email = models.EmailField(max_length=70, blank=True, null=True)
# ForeignKey
# ManyToManyField


class SearchTask(models.Model):
    search_id = models.IntegerField(default="0")
    input_data = models.TextField(default="")  # входные данные в JSON
    output_data_aviasales = models.TextField(default="")  # выходные данные в JSON
    output_data_booking = models.TextField(default="")  # выходные данные в JSON
    output_data_tourvisor = models.TextField(default="")  # выходные данные в JSON
    output_data_rezult = models.TextField(default="")  # выходные данные в JSON
    is_loading_failed = models.BooleanField(default=False)  # ошибка загрузки
    current_status_aviasales = models.CharField(default="new", max_length=8)  # текущий статус: new/work/finish
    current_status_booking = models.CharField(default="new", max_length=8)  # текущий статус: new/work/finish
    current_status_tourvisor = models.CharField(default="new", max_length=8)  # текущий статус: new/work/finish
    current_status_rezult = models.CharField(default="new", max_length=8)  # текущий статус: new/work/finish
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'ID:{0}; search_id:{1}; status_a:{2}; status_b:{3}; status_t:{4}; ' \
               'status_r:{5}; update_time:{6}; input_data:{7}'.format(
            self.pk, self.search_id, self.current_status_aviasales, self.current_status_booking,
            self.current_status_tourvisor, self.current_status_rezult, self.update_time, self.input_data[:60])

# TODO сделать тут модель AviasalesSearchTask добавить флаги
#      is_loading_ended = models.BooleanField(default=False)
#      is_loading_failed = models.BooleanField(default=False)
#      статусы: ожидает, в работе, завершен.
