from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Test, Run


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    ctx = dict()

    if username or password:
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
            'tests' : Test.objects.all(),
            'runs' : Run.objects.all(),
    }

    return render(request, 'overview.html', ctx)


@login_required
def order(request):
    testid = request.POST['testid']
    interviewee = request.POST['interviewee']
    sex = request.POST['sex']

    test = Test.objects.get(pk=testid)

    run = Run(
            user=request.user,
            test=test, 
            iv_id=interviewee,
            iv_male=(sex == '1'))
    run.save()

    return overview(request)


@login_required
def deleterun(request, runid):
    run = Run.objects.get(id=runid)
    run.delete()
    return overview(request)
