from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    ctx = dict()

    if username or password:
        print('###', username, password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return overview(request)
        else:
            ctx['txt_error_msg'] = 'Der Anmeldeversuch ist fehlgeschlagen. ' \
                'Bitte kontrollieren Sie ihre E-Mail-Adresse und das Passwort.'

    ctx.update({
            'txt_title' : 'Dr. Barfuss Anmeldung',
            'txt_username' : 'E-Mail-Adresse',
            'txt_passwd' : 'Passwort',
            'txt_login' : 'Anmelden',
    })

    return render(request, 'login.html', ctx)


def logout(request):
    auth.logout(request)
    return login(request)


@login_required
def overview(request):

    ctx = {
            'txt_title' : 'Dr. Barfuss Übersicht',
    }

    return render(request, 'overview.html', ctx)



