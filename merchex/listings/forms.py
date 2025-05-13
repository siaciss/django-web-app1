from django import forms
from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
    
class BandForm(forms.ModelForm):
    #name = forms.CharField(max_length=100)
    #biography = forms.CharField(max_length=1000)
    #year_formed = forms.IntegerField(min_value=1900, max_value=2100)
    #official_homepage = forms.URLField(required=False)
    class Meta:
        model = Band
        #fields = '__all__'
        #exclude = ('active', 'official_homepage')
        fields = ('name','genre','year_formed','biography')
        widgets = {
            'biography': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 100, 'rows':10})
        }