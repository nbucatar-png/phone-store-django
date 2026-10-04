from django import forms


class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='Имя', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Иван Иванов'}))
    phone = forms.CharField(label='Телефон', max_length=30, widget=forms.TextInput(attrs={'placeholder': '+7 (999) 123-45-67'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com'}))
    address = forms.CharField(label='Адрес доставки', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Город, улица, дом, квартира'}))
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Дополнительная информация'}))
