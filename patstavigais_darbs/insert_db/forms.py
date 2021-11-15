from django.forms import (
    Form,
    CharField,
    EmailField,
)


class CreateUserForm(Form):

    username = CharField()
    e_mail = EmailField()