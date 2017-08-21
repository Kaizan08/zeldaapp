from django import forms
from django.contrib.auth.models import User

from .models import TimezoneChart


# class CustomUserChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         print(obj.get_full_name())
#         return obj.get_full_name()


class UserForm(forms.ModelForm):
    timezone = forms.ModelChoiceField(queryset=TimezoneChart.objects.distinct('name'))

    class Meta:
        model = User
        exclude = ()