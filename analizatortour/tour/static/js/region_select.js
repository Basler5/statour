window.onload = function() {
 if ($("select[name='destination_resort']").val() == "Новый") {
$("select[name='destination_resort']").empty();
        if ($("select[name='destination_country']").val() == "Таиланд") {
            data2 = {
                "Бангкок": "Бангкок",
                "Као Лак": "Као Лак",
                "Ко Чанг": "Ко Чанг",
                "Краби": "Краби",
                "Паттайя": "Паттайя",
                "Пхукет": "Пхукет",
                "Районг": "Районг",
                "Самуи": "Самуи",
                "Хуа Хин": "Хуа Хин",
                "Чианг Май": "Чианг Май",
            };
            def2 = "Пхукет";
        };
        for(var id in data2) {
            if (id == def2) {
                $("select[name='destination_resort']").append($("<option selected value='" + id + "'>" + data2[id] + "</option>"));
            } else {
                $("select[name='destination_resort']").append($("<option value='" + id + "'>" + data2[id] + "</option>"));
            };
        };
    };
};

$(document).ready (function () {
    $("select[name='destination_country']").bind("change", function () {
        $("select[name='destination_resort']").empty();

        if ($("select[name='destination_country']").val() == "Таиланд") {
            data2 = {
                "Бангкок": "Бангкок",
                "Као Лак": "Као Лак",
                "Ко Чанг": "Ко Чанг",
                "Краби": "Краби",
                "Паттайя": "Паттайя",
                "Пхукет": "Пхукет",
                "Районг": "Районг",
                "Самуи": "Самуи",
                "Хуа Хин": "Хуа Хин",
                "Чианг Май": "Чианг Май",
            };
            def2 = "Пхукет";
        };

        if ($("select[name='destination_country']").val() == "Турция") {
            data2 = {
                "Алания": "Алания",
                "Анталия": "Анталия",
                "Белек": "Белек",
                "Бодрум": "Бодрум",
                "Даламан": "Даламан",
                "Дидим": "Дидим",
                "Измир": "Измир",
                "Кайсери": "Кайсери",
                "Каппадокия": "Каппадокия",
                "Кемер": "Кемер",
                "Кушадасы": "Кушадасы",
                "Мармарис": "Мармарис",
                "Сиде": "Сиде",
                "Стамбул": "Стамбул",
                "Улудаг": "Улудаг",
                "Фетхие": "Фетхие",
                "Чешме": "Чешме",
                "Эрзурум": "Эрзурум",
            };
            def2 = "Кемер";
        };

        if ($("select[name='destination_country']").val() == "Филиппины") {
            data2 = {
                "Боракай": "Боракай",
                "Бохоль": "Бохоль",
                "Лусон": "Лусон",
                "Палаван": "Палаван",
                "Себу": "Себу",
            };
            def2 = "Боракай";
        };

        if ($("select[name='destination_country']").val() == "Япония") {
            data2 = {
                "Киото": "Киото",
                "Окинава": "Окинава",
                "Осака": "Осака",
                "Токио": "Токио",
            };
            def2 = "Токио";
        };

        if ($("select[name='destination_country']").val() == "Тунис") {
            data2 = {
                "Гаммарт": "Гаммарт",
                "Джерба": "Джерба",
                "Махдия": "Махдия",
                "Монастир": "Монастир",
                "Сусс": "Сусс",
                "Табарка": "Табарка",
                "Хаммамет": "Хаммамет",
            };
            def2 = "Хаммамет";
        };

        for(var id in data2) {
            if (id == def2) {
                $("select[name='destination_resort']").append($("<option selected value='" + id + "'>" + data2[id] + "</option>"));
            } else {
                $("select[name='destination_resort']").append($("<option value='" + id + "'>" + data2[id] + "</option>"));
            };
        };
    });
});
