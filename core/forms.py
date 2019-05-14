from django.forms import Form, CharField, URLField, TextInput


class ChildForm(Form):
    child_name = CharField(label='Child name', max_length=30,
                           widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Child name'}))
    customer_name = CharField(label='Customer name', max_length=30,
                              widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Site name'}))
    customer_site = URLField(label='Customer site',
                             widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Site url'}))
