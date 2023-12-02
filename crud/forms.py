from django import forms
from .models import *
class create_new_student_form(forms.ModelForm):
    class Meta:
        model=students_data
        fields="__all__"