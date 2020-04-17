from django import forms
import datetime
from .models import SearchRequest, SearchTask

class SearchForm(forms.ModelForm):
    class Meta:
          model = SearchRequest
          fields = ("departure_country",
                      "departure_city",
                      "date_of_departure",
                      "changing_the_departure_date",
                      "destination_country",
                      "destination_resort",
                      "hotel_name",
                      "count_of_hotel_stars",
                      "hotel_rating",
                      "type_of_food",
                      "return_date",
                      "changing_return_date",
                      "number_of_adults",
                      "number_of_children",
                      "number_of_infants",
                      "direct_flights_only",
                      "accommodation_at_the_hotel_only",
                      )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departure_country'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['departure_city'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['date_of_departure'].widget.attrs.update({
            # 'value': datetime.date.today() + datetime.timedelta(days=14),
            'class': 'form-control vDateField',
            'min': datetime.date.today(),
            'max': datetime.date.today() + datetime.timedelta(days=365)})
        self.fields['changing_the_departure_date'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['destination_country'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['destination_resort'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['hotel_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['count_of_hotel_stars'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['hotel_rating'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['type_of_food'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['return_date'].widget.attrs.update({
            'class': 'form-control vDateField',
            'min': datetime.date.today() + datetime.timedelta(days=3),
            'max': datetime.date.today() + datetime.timedelta(days=365)})
        self.fields['changing_return_date'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['number_of_adults'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['number_of_children'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['number_of_infants'].widget.attrs.update({'class': 'custom-select d-block w-100'})
        self.fields['direct_flights_only'].widget.attrs.update({'class': 'custom-control-input'})
        self.fields['accommodation_at_the_hotel_only'].widget.attrs.update({'class': 'custom-control-input'})
        # self.fields['accommodation_at_the_hotel_only'].label.widget.attrs.update({'class': 'custom-control-label'})
