from django import forms
from models import *
from django.contrib.auth.models import User

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('food', 'stars', 'description')
    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args)
        if kwargs.get('user'):
            c_user=kwargs.get('user')
            f = Rating.objects.filter(user=c_user).values_list('food')
            self.fields['food'].queryset = Food.objects.exclude(id__in=f)

