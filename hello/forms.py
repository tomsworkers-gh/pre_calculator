from django import forms

class HelloForm(forms.Form):
    amount = forms.IntegerField(label='積立月額（円）', min_value=1)
    interest = forms.FloatField(label='運用年利（％）')
    period = forms.FloatField(label='積立期間（年）')

class EstimatorForm(forms.Form):
    Monthly = forms.IntegerField(label='積立月額［円］', min_value=1)
    Period = forms.IntegerField(label='期間［年］', min_value=1)
    Finish = forms.IntegerField(label='最終金額［円］', min_value=1)