from .models import Advertisement
from django import forms

class AdsForm(forms.ModelForm):
    class Meta:
        model  = Advertisement
        fields = '__all__'
        exclude = ('ads_status', 'ads_approval_status', 'ads_total_views', 'advertisement_slug')
        help_texts = {
            "weekly_rent": "(in USD $)",
            "bond_amount_required": "(in USD $)"
        }


class AdsDeleteForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = []