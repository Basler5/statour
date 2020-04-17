"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from tour import views as tour_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajax_aviasales/', tour_views.get_result_data_ajax_aviasales),
    path('ajax_booking/', tour_views.get_result_data_ajax_booking),
    path('ajax_tourvisor/', tour_views.get_result_data_ajax_tourvisor),
    path('ajax_rezult/', tour_views.get_result_data_ajax_rezult),
    path('lta/', tour_views.last_task_aviasales),
    path('ltb/', tour_views.last_task_booking),
    path('ltt/', tour_views.last_task_tourvisor),
    path('', include('tour.urls')),
]
