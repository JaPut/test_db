from django.shortcuts import render

from .models import User
from .forms import CreateUserForm


def get_users(request):

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(
        request,
        template_name='users.html',
        context=context,
    )


def add_user(request):

    form = CreateUserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = User(
                username=form.cleaned_data['username'],
                e_mail=form.cleaned_data['e_mail'],
            )

            user.save()

            context = {
                'user': user,
            }

            return render(
                request,
                template_name='user.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_user.html',
        context=context,
    )