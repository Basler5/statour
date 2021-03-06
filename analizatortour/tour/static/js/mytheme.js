"use strict";
! function(e) {
    e.matches = e.matches || e.mozMatchesSelector || e.msMatchesSelector || e.oMatchesSelector || e.webkitMatchesSelector, e.closest = e.closest || function(e) {
        return this ? this.matches(e) ? this : this.parentElement ? this.parentElement.closest(e) : null : null
    }
}(Element.prototype);
var demoMode = function() {
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
        }).popover("show"), i.addEventListener("click", function() {
            $(i).popover("hide"), localStorage.setItem("dashkitShowPopover", !1)
        })),
        function() {
            for (var e = window.location.search.substring(1).split("&"), t = 0; t < e.length; t++) {
                var a = e[t].split("="),
                    o = a[0],
                    l = a[1];
                "colorScheme" != o && "navPosition" != o && "navColor" != o && "sidebarSize" != o || (localStorage.setItem("dashkit" + o.charAt(0).toUpperCase() + o.slice(1), l), S[o] = l)
            }
        }(), "light" == (e = S.colorScheme) ? (y.disabled = !1, C.disabled = !0, e = "light") : "dark" == e && (y.disabled = !0, C.disabled = !1, e = "dark"),
        function(e) {
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
        }(S.navPosition), t = S.navColor, f && h && d && ("default" == t ? (f.classList.add("navbar-light"), h.classList.add("navbar-light"), d.classList.add("navbar-light")) : "inverted" == t ? (f.classList.add("navbar-dark"), h.classList.add("navbar-dark"), d.classList.add("navbar-dark")) : "vibrant" == t && (f.classList.add("navbar-dark", "navbar-vibrant"), h.classList.add("navbar-dark", "navbar-vibrant"), d.classList.add("navbar-dark", "navbar-vibrant"))), "base" == (a = S.sidebarSize) ? A(h) : "small" == a && A(f), o = c, l = S.colorScheme, n = S.navPosition, r = S.navColor, s = S.sidebarSize, $(o).find('[name="colorScheme"][value="' + l + '"]').closest(".btn").button("toggle"), $(o).find('[name="navPosition"][value="' + n + '"]').closest(".btn").button("toggle"), $(o).find('[name="navColor"][value="' + r + '"]').closest(".btn").button("toggle"), $(o).find('[name="sidebarSize"][value="' + s + '"]').closest(".btn").button("toggle"), k(S.navPosition), document.body.style.display = "block", c && (c.addEventListener("submit", function(e) {
            var t, a, o, l, n;
            e.preventDefault(), a = (t = c).querySelector('[name="colorScheme"]:checked').value, o = t.querySelector('[name="navPosition"]:checked').value, l = t.querySelector('[name="navColor"]:checked').value, n = t.querySelector('[name="sidebarSize"]:checked').value, localStorage.setItem("dashkitColorScheme", a), localStorage.setItem("dashkitNavPosition", o), localStorage.setItem("dashkitNavColor", l), localStorage.setItem("dashkitSidebarSize", n), window.location = window.location.pathname
        }), [].forEach.call(v, function(e) {
            e.parentElement.addEventListener("click", function() {
                k(e.value)
            })
        })), !0
}();
! function() {
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
        return Chart.helpers.each(Chart.instances, function(e) {
            t == e.chart.canvas && (a = e)
        }), a
    }
    "undefined" != typeof Chart && (Chart.defaults.global.responsive = !0, Chart.defaults.global.maintainAspectRatio = !1, Chart.defaults.global.defaultColor = e[600], Chart.defaults.global.defaultFontColor = e[600], Chart.defaults.global.defaultFontFamily = l, Chart.defaults.global.defaultFontSize = 13, Chart.defaults.global.layout.padding = 0, Chart.defaults.global.legend.display = !1, Chart.defaults.global.legend.position = "bottom", Chart.defaults.global.legend.labels.usePointStyle = !0, Chart.defaults.global.legend.labels.padding = 16, Chart.defaults.global.elements.point.radius = 0, Chart.defaults.global.elements.point.backgroundColor = t[700], Chart.defaults.global.elements.line.tension = .4, Chart.defaults.global.elements.line.borderWidth = 3, Chart.defaults.global.elements.line.borderColor = t[700], Chart.defaults.global.elements.line.backgroundColor = o, Chart.defaults.global.elements.line.borderCapStyle = "rounded", Chart.defaults.global.elements.rectangle.backgroundColor = t[700], Chart.defaults.global.elements.rectangle.maxBarThickness = 10, Chart.defaults.global.elements.arc.backgroundColor = t[700], Chart.defaults.global.elements.arc.borderColor = a, Chart.defaults.global.elements.arc.borderWidth = 4, Chart.defaults.global.elements.arc.hoverBorderColor = a, Chart.defaults.global.tooltips.enabled = !1, Chart.defaults.global.tooltips.mode = "index", Chart.defaults.global.tooltips.intersect = !1, Chart.defaults.global.tooltips.custom = function(n) {
        var e = document.getElementById("chart-tooltip"),
            r = this._chart.config.type;
        if (e || ((e = document.createElement("div")).setAttribute("id", "chart-tooltip"), e.setAttribute("role", "tooltip"), e.classList.add("popover"), e.classList.add("bs-popover-top"), document.body.appendChild(e)), 0 !== n.opacity) {
            if (n.body) {
                var t = n.title || [],
                    a = n.body.map(function(e) {
                        return e.lines
                    }),
                    s = '<div class="arrow"></div>';
                t.forEach(function(e) {
                    s += '<h3 class="popover-header text-center">' + e + "</h3>"
                }), a.forEach(function(e, t) {
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
    }, Chart.defaults.global.tooltips.callbacks.label = function(e, t) {
        var a = "",
            o = e.yLabel,
            l = t.datasets[e.datasetIndex],
            n = l.label,
            r = l.yAxisID ? l.yAxisID : 0,
            s = this._chart.options.scales.yAxes,
            i = s[0];
        if (r) i = s.filter(function(e) {
            return e.id == r
        })[0];
        var c = i.ticks.callback;
        return 1 < t.datasets.filter(function(e) {
            return !e.hidden
        }).length && (a = '<span class="popover-body-label mr-auto">' + n + "</span>"), a += '<span class="popover-body-value">' + c(o) + "</span>"
    }, Chart.defaults.doughnut.cutoutPercentage = 83, Chart.defaults.doughnut.tooltips.callbacks.title = function(e, t) {
        return t.labels[e[0].index]
    }, Chart.defaults.doughnut.tooltips.callbacks.label = function(e, t) {
        var a = t.datasets[0].data[e.index],
            o = this._chart.options.tooltips.callbacks,
            l = o.afterLabel() ? o.afterLabel() : "";
        return '<span class="popover-body-value">' + (o.beforeLabel() ? o.beforeLabel() : "") + a + l + "</span>"
    }, Chart.defaults.doughnut.legendCallback = function(e) {
        var o = e.data,
            l = "";
        return o.labels.forEach(function(e, t) {
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
    }), n && [].forEach.call(n, function(e) {
        var t = e.dataset.trigger;
        e.addEventListener(t, function() {
            ! function(e) {
                var t = e.dataset.target,
                    a = e.dataset.action,
                    o = parseInt(e.dataset.dataset),
                    l = f(document.querySelector(t));
                if ("toggle" === a) {
                    var n = l.data.datasets,
                        r = n.filter(function(e) {
                            return !e.hidden
                        })[0],
                        s = n.filter(function(e) {
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
    }), r && document.addEventListener("DOMContentLoaded", function() {
        [].forEach.call(r, function(e) {
            var t, a, o;
            a = f(t = e).generateLegend(), o = t.dataset.target, document.querySelector(o).innerHTML = a
        })
    }))
}(),
function() {
    var e = {
            300: "#E3EBF6",
            600: "#95AAC9",
            700: "#6E84A3",
            800: "#152E4D",
            900: "#283E59"
        },
        t = localStorage.getItem("dashkitColorScheme") ? localStorage.getItem("dashkitColorScheme") : "light";

    function a() {
        Chart.defaults.global.defaultColor = e[700], Chart.defaults.global.defaultFontColor = e[700], Chart.defaults.global.elements.arc.borderColor = e[800], Chart.defaults.global.elements.arc.hoverBorderColor = e[800], Chart.scaleService.updateScaleDefaults("linear", {
            gridLines: {
                borderDash: [2],
                borderDashOffset: [2],
                color: e[900],
                drawBorder: !1,
                drawTicks: !1,
                zeroLineColor: e[900],
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2]
            },
            ticks: {
                beginAtZero: !0,
                padding: 10,
                callback: function(e) {
                    if (!(e % 10)) return e
                }
            }
        })
    }
    "undefined" != typeof Chart && (void 0 === demoMode ? a() : demoMode && "dark" == t && a())
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="autosize"]');
    "undefined" != typeof autosize && e && [].forEach.call(e, function(e) {
        autosize(e)
    })
}(),
function() {
    var e = document.getElementById("audienceChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "line",
        options: {
            scales: {
                yAxes: [{
                    id: "yAxisOne",
                    type: "linear",
                    display: "auto",
                    gridLines: {
                        color: "#283E59",
                        zeroLineColor: "#283E59"
                    },
                    ticks: {
                        callback: function(e) {
                            return e + "k"
                        }
                    }
                }, {
                    id: "yAxisTwo",
                    type: "linear",
                    display: "auto",
                    gridLines: {
                        color: "#283E59",
                        zeroLineColor: "#283E59"
                    },
                    ticks: {
                        callback: function(e) {
                            return e + "%"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [{
                label: "Customers",
                data: [0, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 40],
                yAxisID: "yAxisOne"
            }, {
                label: "Sessions",
                data: [50, 75, 35, 25, 55, 87, 67, 53, 25, 80, 87, 45],
                yAxisID: "yAxisOne",
                hidden: !0
            }, {
                label: "Conversion",
                data: [40, 57, 25, 50, 57, 32, 46, 28, 59, 34, 52, 48],
                yAxisID: "yAxisTwo",
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("conversionsChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "bar",
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        callback: function(e) {
                            return e + "%"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Oct 1", "Oct 2", "Oct 3", "Oct 4", "Oct 5", "Oct 6", "Oct 7", "Oct 8", "Oct 9", "Oct 10", "Oct 11", "Oct 12"],
            datasets: [{
                label: "2020",
                data: [25, 20, 30, 22, 17, 10, 18, 26, 28, 26, 20, 32]
            }, {
                label: "2019",
                data: [15, 10, 20, 12, 7, 0, 8, 16, 18, 16, 10, 22],
                backgroundColor: "#d2ddec",
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("trafficChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "doughnut",
        options: {
            tooltips: {
                callbacks: {
                    afterLabel: function() {
                        return "%"
                    }
                }
            }
        },
        data: {
            labels: ["Тур", "Билеты", "Отель"],
            datasets: [{
                data: [60, 25, 15],
                backgroundColor: ["#2C7BE5", "#A6C5F7", "#D2DDEC"]
            }, {
                data: [15, 45, 20],
                backgroundColor: ["#2C7BE5", "#A6C5F7", "#D2DDEC"],
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("trafficChartAlt");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "doughnut",
        options: {
            tooltips: {
                callbacks: {
                    afterLabel: function() {
                        return "%"
                    }
                }
            }
        },
        data: {
            labels: ["ТурР", "БилетыЫ", "ОтельЬ"],
            datasets: [{
                data: [60, 25, 15],
                backgroundColor: ["#2C7BE5", "#A6C5F7", "#D2DDEC"]
            }, {
                data: [15, 45, 20],
                backgroundColor: ["#2C7BE5", "#A6C5F7", "#D2DDEC"],
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("salesChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "line",
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        callback: function(e) {
                            return "$" + e + "k"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Oct 1", "Oct 3", "Oct 6", "Oct 9", "Oct 12", "Oct 5", "Oct 18", "Oct 21", "Oct 24", "Oct 27", "Oct 30"],
            datasets: [{
                label: "All",
                data: [0, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25]
            }, {
                label: "Tour",
                data: [7, 40, 12, 27, 34, 17, 19, 30, 28, 32, 24],
                hidden: !0
            }, {
                label: "Tikets",
                data: [2, 12, 35, 25, 36, 25, 34, 16, 4, 14, 15],
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("ordersChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "bar",
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        callback: function(e) {
                            return "$" + e + "k"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [{
                label: "Sales",
                data: [25, 20, 30, 22, 17, 10, 18, 26, 28, 26, 20, 32]
            }, {
                label: "Affiliate",
                data: [15, 10, 20, 12, 7, 0, 8, 16, 18, 16, 10, 22],
                backgroundColor: "#d2ddec",
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("earningsChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "bar",
        options: {
            scales: {
                yAxes: [{
                    id: "yAxisOne",
                    type: "linear",
                    display: "auto",
                    ticks: {
                        callback: function(e) {
                            return "$" + e + "k"
                        }
                    }
                }, {
                    id: "yAxisTwo",
                    type: "linear",
                    display: "auto",
                    ticks: {
                        callback: function(e) {
                            return e + "k"
                        }
                    }
                }, {
                    id: "yAxisThree",
                    type: "linear",
                    display: "auto",
                    ticks: {
                        callback: function(e) {
                            return e + "%"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            datasets: [{
                label: "Earnings",
                data: [18, 10, 5, 15, 10, 20, 15, 25, 20, 26, 25, 29, 18, 10, 5, 15, 10, 20],
                yAxisID: "yAxisOne"
            }, {
                label: "Sessions",
                data: [50, 75, 35, 25, 55, 87, 67, 53, 25, 80, 87, 45, 50, 75, 35, 25, 55, 19],
                yAxisID: "yAxisTwo",
                hidden: !0
            }, {
                label: "Bounce",
                data: [40, 57, 25, 50, 57, 32, 46, 28, 59, 34, 52, 48, 40, 57, 25, 50, 57, 29],
                yAxisID: "yAxisThree",
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("weeklyHoursChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "bar",
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        callback: function(e) {
                            return e + "hrs"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            datasets: [{
                data: [21, 12, 28, 15, 5, 12, 17, 2]
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("overviewChart");
    e && new Chart(e, {
        type: "line",
        options: {
            scales: {
                yAxes: [{
                    id: "yAxisOne",
                    type: "linear",
                    display: "auto",
                    ticks: {
                        callback: function(e) {
                            return "$" + e + "k"
                        }
                    }
                }, {
                    id: "yAxisTwo",
                    type: "linear",
                    display: "auto",
                    ticks: {
                        callback: function(e) {
                            return e + "hrs"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [{
                label: "Earned",
                data: [0, 10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 40],
                yAxisID: "yAxisOne"
            }, {
                label: "Hours Worked",
                data: [7, 35, 12, 27, 34, 17, 19, 30, 28, 32, 24, 39],
                yAxisID: "yAxisTwo",
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.getElementById("sparklineChart");
    "undefined" != typeof Chart && e && new Chart(e, {
        type: "line",
        options: {
            scales: {
                yAxes: [{
                    display: !1
                }],
                xAxes: [{
                    display: !1
                }]
            },
            elements: {
                line: {
                    borderWidth: 2
                },
                point: {
                    hoverRadius: 0
                }
            },
            tooltips: {
                custom: function() {
                    return !1
                }
            }
        },
        data: {
            labels: new Array(12),
            datasets: [{
                data: [0, 15, 10, 25, 30, 15, 40, 50, 80, 60, 55, 65]
            }]
        }
    })
}(),
function() {
    var e = document.querySelectorAll("#sparklineChartSocialOne, #sparklineChartSocialTwo, #sparklineChartSocialThree, #sparklineChartSocialFour");
    "undefined" != typeof Chart && e && [].forEach.call(e, function(e) {
        new Chart(e, {
            type: "line",
            options: {
                scales: {
                    yAxes: [{
                        display: !1
                    }],
                    xAxes: [{
                        display: !1
                    }]
                },
                elements: {
                    line: {
                        borderWidth: 2,
                        borderColor: "#D2DDEC"
                    },
                    point: {
                        hoverRadius: 0
                    }
                },
                tooltips: {
                    custom: function() {
                        return !1
                    }
                }
            },
            data: {
                labels: new Array(12),
                datasets: [{
                    data: [0, 15, 10, 25, 30, 15, 40, 50, 80, 60, 55, 65]
                }]
            }
        })
    })
}(),
function() {
    var e = document.getElementById("feedChart");
    e && new Chart(e, {
        type: "bar",
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        callback: function(e) {
                            return "$" + e + "k"
                        }
                    }
                }]
            }
        },
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [{
                label: "Sales",
                data: [25, 20, 30, 22, 17, 10, 18, 26, 28, 26, 20, 32]
            }, {
                label: "Affiliate",
                data: [15, 10, 20, 12, 7, 0, 8, 16, 18, 16, 10, 22],
                backgroundColor: "#d2ddec",
                hidden: !0
            }]
        }
    })
}(),
function() {
    var e = document.querySelectorAll('[name="ordersSelect"]'),
        t = document.getElementById("ordersSelectAll");
    e && t && t.addEventListener("change", function() {
        var t = this;
        [].forEach.call(e, function(e) {
            e.checked = t.checked
        })
    })
}(),
function() {
    var e = document.querySelectorAll(".dropup, .dropright, .dropdown, .dropleft"),
        t = document.querySelectorAll(".dropdown-menu .dropdown-toggle");
    t && [].forEach.call(t, function(l) {
        l.addEventListener("click", function(e) {
            var t, a, o;
            e.preventDefault(), a = (t = l).parentElement.querySelector(".dropdown-menu"), o = t.closest(".dropdown-menu").querySelectorAll(".dropdown-menu"), [].forEach.call(o, function(e) {
                e !== a && e.classList.remove("show")
            }), a.classList.toggle("show"), e.stopPropagation()
        })
    }), $(e).on("hide.bs.dropdown", function() {
        var e;
        (e = this.querySelectorAll(".dropdown-menu")) && [].forEach.call(e, function(e) {
            e.classList.remove("show")
        })
    })
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="dropzone"]');
    "undefined" != typeof Dropzone && e && (Dropzone.autoDiscover = !1, Dropzone.thumbnailWidth = null, Dropzone.thumbnailHeight = null, [].forEach.call(e, function(e) {
        ! function(e) {
            var t = void 0,
                a = e.dataset.options;
            a = a ? JSON.parse(a) : {};
            var o = {
                    previewsContainer: e.querySelector(".dz-preview"),
                    previewTemplate: e.querySelector(".dz-preview").innerHTML,
                    init: function() {
                        this.on("addedfile", function(e) {
                            1 == a.maxFiles && t && this.removeFile(t), t = e
                        })
                    }
                },
                l = Object.assign(o, a);
            e.querySelector(".dz-preview").innerHTML = "", new Dropzone(e, l)
        }(e)
    }))
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="flatpickr"]');
    "undefined" != typeof flatpickr && e && [].forEach.call(e, function(e) {
        var t, a;
        a = (a = (t = e).dataset.options) ? JSON.parse(a) : {}, flatpickr(t, a)
    })
}(),
function() {
    var e = document.querySelectorAll(".highlight");
    "undefined" != typeof hljs && e && [].forEach.call(e, function(e) {
        var t;
        t = e, hljs.highlightBlock(t)
    })
}(),
function() {
    var e = document.querySelectorAll(".kanban-category"),
        t = document.querySelectorAll(".kanban-add-link"),
        a = document.querySelectorAll(".kanban-add-form");

    function o(e) {
        var t = e.closest(".kanban-add"),
            a = t.querySelector(".card"),
            o = t.querySelector(".kanban-add-link"),
            l = t.querySelector(".kanban-add-form");
        o.classList.toggle("d-none"), l.classList.toggle("d-none"), a && a.classList.contains("card-sm") && (a.classList.contains("card-flush") ? a.classList.remove("card-flush") : a.classList.add("card-flush"))
    }
    "undefined" != typeof Draggable && e && new Draggable.Sortable(e, {
        draggable: ".kanban-item",
        mirror: {
            constrainDimensions: !0
        }
    }), t && [].forEach.call(t, function(e) {
        e.addEventListener("click", function() {
            o(e)
        })
    }), a && [].forEach.call(a, function(e) {
        e.addEventListener("reset", function() {
            o(e)
        }), e.addEventListener("submit", function(e) {
            e.preventDefault()
        })
    })
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="lists"]'),
        t = document.querySelectorAll('[data-toggle="lists"] [data-sort]');
    "undefined" != typeof List && (e && [].forEach.call(e, function(e) {
        var t, a;
        a = (t = e).dataset.options ? JSON.parse(t.dataset.options) : {}, new List(t, a)
    }), t && [].forEach.call(t, function(e) {
        e.addEventListener("click", function(e) {
            e.preventDefault()
        })
    }))
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="map"]');
    "undefined" != typeof mapboxgl && e && [].forEach.call(e, function(e) {
        ! function(e) {
            var t = e.dataset.options;
            t = t ? JSON.parse(t) : {};
            var a = {
                    container: e,
                    style: "mapbox://styles/mapbox/light-v9",
                    scrollZoom: !1,
                    interactive: !1
                },
                o = Object.assign(a, t);
            mapboxgl.accessToken = "pk.eyJ1IjoiZ29vZHRoZW1lcyIsImEiOiJjanU5eHR4N2cybDU5NGVwOHZwNGprb3E0In0.msdw9q16dh8v4azJXUdiXg", new mapboxgl.Map(o)
        }(e)
    })
}(),
function() {
    var e = document.querySelectorAll('.navbar-nav [data-toggle="collapse"]');
    [].forEach.call(e, function(a) {
        a.addEventListener("click", function() {
            var t, e;
            e = (t = a).closest(".collapse").querySelectorAll(".collapse"), [].forEach.call(e, function(e) {
                e !== t && $(e).collapse("hide")
            })
        })
    })
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="popover"]');
    e && $(e).popover()
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="quill"]');
    "undefined" != typeof Quill && e && [].forEach.call(e, function(e) {
        ! function(e) {
            var t = e.dataset.options;
            t = t ? JSON.parse(t) : {};
            var a = Object.assign({
                modules: {
                    toolbar: [
                        ["bold", "italic"],
                        ["link", "blockquote", "code", "image"],
                        [{
                            list: "ordered"
                        }, {
                            list: "bullet"
                        }]
                    ]
                },
                theme: "snow"
            }, t);
            new Quill(e, a)
        }(e)
    })
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="select"]');

    function n(e) {
        if (!e.id || !e.element || !e.element.dataset.avatarSrc) return e.text;
        var t = e.element.dataset.avatarSrc,
            a = document.createElement("div");
        return a.innerHTML = '<span class="avatar avatar-xs mr-3"><img class="avatar-img rounded-circle" src="' + t + '" alt="' + e.text + '"></span><span>' + e.text + "</span>", a
    }
    jQuery().select2 && e && [].forEach.call(e, function(e) {
        var t, a, o, l;
        a = (t = e).dataset.options ? JSON.parse(t.dataset.options) : {}, o = {
            containerCssClass: t.getAttribute("class"),
            dropdownCssClass: "dropdown-menu show",
            dropdownParent: t.closest(".modal") ? t.closest(".modal") : document.body,
            templateResult: n
        }, l = Object.assign(o, a), $(t).select2(l)
    })
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="tooltip"]');
    e && $(e).tooltip()
}(),
function() {
    var e = document.querySelectorAll(".checklist");
    "undefined" != typeof Draggable && e && new Draggable.Sortable(e, {
        draggable: ".checklist-control",
        handle: ".custom-control-caption",
        mirror: {
            constrainDimensions: !0
        }
    })
}(),
function() {
    var e = document.querySelectorAll('[data-toggle="wizard"]');
    [].forEach.call(e, function(t) {
        t.addEventListener("click", function(e) {
            e.preventDefault(), $(t).tab("show").removeClass("active")
        })
    })
}();