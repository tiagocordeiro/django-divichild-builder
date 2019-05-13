from django.forms import Form, CharField, URLField


class ChildForm(Form):
    child_name = CharField(label='Child name', max_length=30)
    customer_name = CharField(label='Customer name', max_length=30)
    customer_site = URLField(label='Customer site')
