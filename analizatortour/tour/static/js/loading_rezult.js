
$(document).ready(
    function(){
var i = 0, howManyTimes = 30;
f();
function f() {
        var request = new XMLHttpRequest();
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('search_id');
        request.open("GET", "/ajax_rezult/?search_id="+id);
        request.send();
        request.onreadystatechange=function(){
            if(this.readyState==4 && this.status==200){
                var rez = JSON.parse(request.responseText);
                if (rez.current_status=="finish"){
                    // console.log(rez.data.self_id);
                    var price_tour = rez.rdt_price_for_tour;
                    var price_booking = rez.rdb_rezult_with_tax;
                    var price_avia = rez.rda_lowest_price;
                    howManyTimes = 0;
                    $("div[name='page_header_rezult']").empty();
                    $("div[name='page_header_rezult']").append(
                        $("<h3 class=\"card-header-title badgers badge-soft-success\" ><strong>" + rez.header_text + "</strong></h3>"));

                    $("div[name='page_rezult']").empty();

                    $("div[name='page_rezult']").append(
                        $("<table class='col'>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Стоимость путешествия туром:</td>\n" +
                                "<td><strong>" + rez.rdt_price_for_tour + "</strong><span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"3\"></td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Стоимость проживания, если покупать отдельно:</td>\n" +
                                "<td><strong>" + rez.rdb_rezult_with_tax + "</strong><span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "<tr>\n" +
                                "<td colspan=\"2\">Стоимость перелета, если покупать отдельно:</td>\n" +
                                "<td><strong>" + rez.rda_lowest_price + "</strong><span class=\"h2 rubznak-slim-rub text-muted mb-0\"></span>" +
                                "</td>\n" +
                                "</tr>\n" +
                                "</table>")
                        );

                    $("div[name='page_rezult_price']").empty();
                    $("div[name='page_rezult_price']").append(
                         $("<div class=\"col-auto\"><span class=\"h2\">" +
                           "Итоговая стоимость: <strong>" + rez.rezult_price + "</strong></span>\n" +
                           "<span class=\"h2 rubznak-rub text-muted mb-0\"></span>\n" +
                           "<span class=\"badge badge-soft-success mt-n1\">" + rez.rezult_difference + "</span></div>")
                            );
                }
            }
        }
    i++;
    if( i < howManyTimes ){
        setTimeout( f, 3000 );
    }
    else{
        if(howManyTimes != 0){
            $("div[name='page_rezult']").empty();
            $("div[name='page_rezult']").append(
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

"use strict";
    !function (e) {
        e.matches = e.matches || e.mozMatchesSelector || e.msMatchesSelector || e.oMatchesSelector || e.webkitMatchesSelector, e.closest = e.closest || function (e) {
            return this ? this.matches(e) ? this : this.parentElement ? this.parentElement.closest(e) : null : null
        }
    }(Element.prototype);
    var demoMode = function () {
        var e, t, a, o, l, n, r, s, i = document.querySelector("#popoverDemo"),
            c = document.querySelector("#demoForm"),
            d = document.querySelector("#topnav"),
            u = document.querySelector("#topbar"),
            f = document.querySelector("#sidebar"),
            h = document.querySelector("#sidebarSmall"),
            p = document.querySelector("#sidebarUser"),
            b = document.querySelector("#sidebarSmallUser"),
            g = document.querySelector("#sidebarSizeContainer"),
            v = document.querySelectorAll('input[name="navPosition"]'),
            m = document.querySelectorAll('[class^="container"]'),
            y = document.querySelector("#stylesheetLight"),
            C = document.querySelector("#stylesheetDark"),
            S = {
                showPopover: !localStorage.getItem("dashkitShowPopover") || localStorage.getItem("dashkitShowPopover"),
                colorScheme: localStorage.getItem("dashkitColorScheme") ? localStorage.getItem("dashkitColorScheme") : "light",
                navPosition: localStorage.getItem("dashkitNavPosition") ? localStorage.getItem("dashkitNavPosition") : "sidenav",
                navColor: localStorage.getItem("dashkitNavColor") ? localStorage.getItem("dashkitNavColor") : "default",
                sidebarSize: localStorage.getItem("dashkitSidebarSize") ? localStorage.getItem("dashkitSidebarSize") : "base"
            };

        function k(e) {
            "topnav" == e ? $(g).collapse("hide") : $(g).collapse("show")
        }

        function A(e) {
            e && e.setAttribute("style", "display: none !important")
        }

        return i && (JSON.parse(S.showPopover) && "base" === S.sidebarSize && $(i).popover({
            boundary: "viewport",
            offset: "50px",
            placement: "top",
            template: '<div class="popover popover-lg popover-dark d-none d-md-block" role="tooltip"><div class="arrow"></div><h3 class="popover-header"></h3><div class="popover-body"></div></div>'
        }).popover("show"), i.addEventListener("click", function () {
            $(i).popover("hide"), localStorage.setItem("dashkitShowPopover", !1)
        })),
            function () {
                for (var e = window.location.search.substring(1).split("&"), t = 0; t < e.length; t++) {
                    var a = e[t].split("="),
                        o = a[0],
                        l = a[1];
                    "colorScheme" != o && "navPosition" != o && "navColor" != o && "sidebarSize" != o || (localStorage.setItem("dashkit" + o.charAt(0).toUpperCase() + o.slice(1), l), S[o] = l)
                }
            }(), "light" == (e = S.colorScheme) ? (y.disabled = !1, C.disabled = !0, e = "light") : "dark" == e && (y.disabled = !0, C.disabled = !1, e = "dark"),
            function (e) {
                if (d && u && f && h && p && b)
                    if ("topnav" == e) {
                        A(u), A(f), A(h);
                        for (var t = 0; t < m.length; t++) m[t].classList.remove("container-fluid"), m[t].classList.add("container")
                    } else if ("combo" == e) {
                        A(d), A(p), A(b);
                        for (t = 0; t < m.length; t++) m[t].classList.remove("container"), m[t].classList.add("container-fluid")
                    } else if ("sidenav" == e) {
                        A(d), A(u);
                        for (t = 0; t < m.length; t++) m[t].classList.remove("container"), m[t].classList.add("container-fluid")
                    }
            }(S.navPosition), t = S.navColor, f && h && d && ("default" == t ? (f.classList.add("navbar-light"), h.classList.add("navbar-light"), d.classList.add("navbar-light")) : "inverted" == t ? (f.classList.add("navbar-dark"), h.classList.add("navbar-dark"), d.classList.add("navbar-dark")) : "vibrant" == t && (f.classList.add("navbar-dark", "navbar-vibrant"), h.classList.add("navbar-dark", "navbar-vibrant"), d.classList.add("navbar-dark", "navbar-vibrant"))), "base" == (a = S.sidebarSize) ? A(h) : "small" == a && A(f), o = c, l = S.colorScheme, n = S.navPosition, r = S.navColor, s = S.sidebarSize, $(o).find('[name="colorScheme"][value="' + l + '"]').closest(".btn").button("toggle"), $(o).find('[name="navPosition"][value="' + n + '"]').closest(".btn").button("toggle"), $(o).find('[name="navColor"][value="' + r + '"]').closest(".btn").button("toggle"), $(o).find('[name="sidebarSize"][value="' + s + '"]').closest(".btn").button("toggle"), k(S.navPosition), document.body.style.display = "block", c && (c.addEventListener("submit", function (e) {
            var t, a, o, l, n;
            e.preventDefault(), a = (t = c).querySelector('[name="colorScheme"]:checked').value, o = t.querySelector('[name="navPosition"]:checked').value, l = t.querySelector('[name="navColor"]:checked').value, n = t.querySelector('[name="sidebarSize"]:checked').value, localStorage.setItem("dashkitColorScheme", a), localStorage.setItem("dashkitNavPosition", o), localStorage.setItem("dashkitNavColor", l), localStorage.setItem("dashkitSidebarSize", n), window.location = window.location.pathname
        }), [].forEach.call(v, function (e) {
            e.parentElement.addEventListener("click", function () {
                k(e.value)
            })
        })), !0
    }();
    !function () {
        var e = {
                300: "#E3EBF6",
                600: "#95AAC9",
                700: "#6E84A3",
                800: "#152E4D",
                900: "#283E59"
            },
            t = {
                100: "#D2DDEC",
                300: "#A6C5F7",
                700: "#2C7BE5"
            },
            a = "#FFFFFF",
            o = "transparent",
            l = "Cerebri Sans",
            n = document.querySelectorAll('[data-toggle="chart"]'),
            r = document.querySelectorAll('[data-toggle="legend"]');

        function f(t) {
            var a = void 0;
            return Chart.helpers.each(Chart.instances, function (e) {
                t == e.chart.canvas && (a = e)
            }), a
        }

        "undefined" != typeof Chart && (Chart.defaults.global.responsive = !0, Chart.defaults.global.maintainAspectRatio = !1, Chart.defaults.global.defaultColor = e[600], Chart.defaults.global.defaultFontColor = e[600], Chart.defaults.global.defaultFontFamily = l, Chart.defaults.global.defaultFontSize = 13, Chart.defaults.global.layout.padding = 0, Chart.defaults.global.legend.display = !1, Chart.defaults.global.legend.position = "bottom", Chart.defaults.global.legend.labels.usePointStyle = !0, Chart.defaults.global.legend.labels.padding = 16, Chart.defaults.global.elements.point.radius = 0, Chart.defaults.global.elements.point.backgroundColor = t[700], Chart.defaults.global.elements.line.tension = .4, Chart.defaults.global.elements.line.borderWidth = 3, Chart.defaults.global.elements.line.borderColor = t[700], Chart.defaults.global.elements.line.backgroundColor = o, Chart.defaults.global.elements.line.borderCapStyle = "rounded", Chart.defaults.global.elements.rectangle.backgroundColor = t[700], Chart.defaults.global.elements.rectangle.maxBarThickness = 10, Chart.defaults.global.elements.arc.backgroundColor = t[700], Chart.defaults.global.elements.arc.borderColor = a, Chart.defaults.global.elements.arc.borderWidth = 4, Chart.defaults.global.elements.arc.hoverBorderColor = a, Chart.defaults.global.tooltips.enabled = !1, Chart.defaults.global.tooltips.mode = "index", Chart.defaults.global.tooltips.intersect = !1, Chart.defaults.global.tooltips.custom = function (n) {
            var e = document.getElementById("chart-tooltip"),
                r = this._chart.config.type;
            if (e || ((e = document.createElement("div")).setAttribute("id", "chart-tooltip"), e.setAttribute("role", "tooltip"), e.classList.add("popover"), e.classList.add("bs-popover-top"), document.body.appendChild(e)), 0 !== n.opacity) {
                if (n.body) {
                    var t = n.title || [],
                        a = n.body.map(function (e) {
                            return e.lines
                        }),
                        s = '<div class="arrow"></div>';
                    t.forEach(function (e) {
                        s += '<h3 class="popover-header text-center">' + e + "</h3>"
                    }), a.forEach(function (e, t) {
                        var a = n.labelColors[t],
                            o = '<span class="popover-body-indicator" style="background-color: ' + ("line" === r && "rgba(0,0,0,0.1)" !== a.borderColor ? a.borderColor : a.backgroundColor) + '"></span>',
                            l = 1 < e.length ? "justify-content-left" : "justify-content-center";
                        s += '<div class="popover-body d-flex align-items-center ' + l + '">' + o + e + "</div>"
                    }), e.innerHTML = s
                }
                var o = this._chart.canvas.getBoundingClientRect(),
                    l = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0,
                    i = window.pageXOffset || document.documentElement.scrollLeft || document.body.scrollLeft || 0,
                    c = o.top + l,
                    d = o.left + i,
                    u = e.offsetWidth,
                    f = e.offsetHeight,
                    h = c + n.caretY - f - 16,
                    p = d + n.caretX - u / 2;
                e.style.top = h + "px", e.style.left = p + "px", e.style.visibility = "visible"
            } else e.style.visibility = "hidden"
        }, Chart.defaults.global.tooltips.callbacks.label = function (e, t) {
            var a = "",
                o = e.yLabel,
                l = t.datasets[e.datasetIndex],
                n = l.label,
                r = l.yAxisID ? l.yAxisID : 0,
                s = this._chart.options.scales.yAxes,
                i = s[0];
            if (r) i = s.filter(function (e) {
                return e.id == r
            })[0];
            var c = i.ticks.callback;
            return 1 < t.datasets.filter(function (e) {
                return !e.hidden
            }).length && (a = '<span class="popover-body-label mr-auto">' + n + "</span>"), a += '<span class="popover-body-value">' + c(o) + "</span>"
        }, Chart.defaults.doughnut.cutoutPercentage = 83, Chart.defaults.doughnut.tooltips.callbacks.title = function (e, t) {
            return t.labels[e[0].index]
        }, Chart.defaults.doughnut.tooltips.callbacks.label = function (e, t) {
            var a = t.datasets[0].data[e.index],
                o = this._chart.options.tooltips.callbacks,
                l = o.afterLabel() ? o.afterLabel() : "";
            return '<span class="popover-body-value">' + (o.beforeLabel() ? o.beforeLabel() : "") + a + l + "</span>"
        }, Chart.defaults.doughnut.legendCallback = function (e) {
            var o = e.data,
                l = "";
            return o.labels.forEach(function (e, t) {
                var a = o.datasets[0].backgroundColor[t];
                l += '<span class="chart-legend-item">', l += '<i class="chart-legend-indicator" style="background-color: ' + a + '"></i>', l += e, l += "</span>"
            }), l
        }, Chart.scaleService.updateScaleDefaults("linear", {
            gridLines: {
                borderDash: [2],
                borderDashOffset: [2],
                color: e[300],
                drawBorder: !1,
                drawTicks: !1,
                zeroLineColor: e[300],
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2]
            },
            ticks: {
                beginAtZero: !0,
                padding: 10,
                stepSize: 10
            }
        }), Chart.scaleService.updateScaleDefaults("category", {
            gridLines: {
                drawBorder: !1,
                drawOnChartArea: !1,
                drawTicks: !1
            },
            ticks: {
                padding: 20
            }
        }), n && [].forEach.call(n, function (e) {
            var t = e.dataset.trigger;
            e.addEventListener(t, function () {
                !function (e) {
                    var t = e.dataset.target,
                        a = e.dataset.action,
                        o = parseInt(e.dataset.dataset),
                        l = f(document.querySelector(t));
                    if ("toggle" === a) {
                        var n = l.data.datasets,
                            r = n.filter(function (e) {
                                return !e.hidden
                            })[0],
                            s = n.filter(function (e) {
                                return 1e3 === e.order
                            })[0];
                        if (!s) {
                            for (var i in s = {}, r) "_meta" !== i && (s[i] = r[i]);
                            s.order = 1e3, s.hidden = !0, n.push(s)
                        }
                        var c = n[o] === r ? s : n[o];
                        for (var i in r) "_meta" !== i && (r[i] = c[i]);
                        l.update()
                    }
                    if ("add" === a) {
                        var d = l.data.datasets[o],
                            u = d.hidden;
                        d.hidden = !u
                    }
                    l.update()
                }(e)
            })
        }), r && document.addEventListener("DOMContentLoaded", function () {
            [].forEach.call(r, function (e) {
                var t, a, o;
                a = f(t = e).generateLegend(), o = t.dataset.target, document.querySelector(o).innerHTML = a
            })
        }))
    }(),
        function () {
            var e = document.getElementById("trafficChart");
            "undefined" != typeof Chart && e && new Chart(e, {
                type: "doughnut",
                options: {
                    tooltips: {
                        callbacks: {
                            afterLabel: function () {
                                return "%"
                            }
                        }
                    }
                },

                data: {
                    labels: ["Тур", "Проживание", "Перелет"],
                    datasets: [{
                        data: [
                            90,
                            73,
                            37],
                        backgroundColor: ["#2C7BE5", "#A6C5F7", "#D2DDEC"]
                    }]
                }
            })
        }();