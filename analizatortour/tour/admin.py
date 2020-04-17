from django.contrib import admin
from .models import SearchRequest, SearchTask

admin.site.register(SearchRequest)
admin.site.register(SearchTask)