from django.shortcuts import render


def login(request):
    ctx = {
            'txt_title' : 'Dr. Barfuss Anmeldung',
            'txt_username' : 'E-Mail-Adresse',
            'txt_passwd' : 'Passwort',
            'txt_login' : 'Anmelden',
    }
    return render(request, 'login.html', ctx)


def confirm_login(request):
    return render(request, 'login.html', dict())
