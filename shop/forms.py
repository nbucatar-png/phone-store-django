from django import forms


class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='Full name', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Alex Johnson', 'autocomplete': 'name'}))
    phone = forms.CharField(label='Phone number', max_length=30, widget=forms.TextInput(attrs={'placeholder': '+1 (555) 123-4567', 'autocomplete': 'tel'}))
    email = forms.EmailField(label='Email address', required=False, widget=forms.EmailInput(attrs={'placeholder': 'you@example.com', 'autocomplete': 'email'}))
    address = forms.CharField(label='Delivery address', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Street, city, ZIP code', 'autocomplete': 'street-address'}))
    comment = forms.CharField(label='Order notes', required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Anything we should know?'}))
