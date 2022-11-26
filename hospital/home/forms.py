from django import forms
from . models import Booking


class Calender(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date':Calender()
        }

        labels={
            'p_name':'Patient Name',
            'p_phone':'Phone No.',
            'p_email':'Email Id',
            'dpt_name':'Department Name',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date'
        }