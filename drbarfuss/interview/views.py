import importlib

from django.shortcuts import render
from enquirer.models import Run


def ask(request, runkey, index):
    run = Run.objects.get(key=runkey)
    module = importlib.import_module(run.test.module)
    return module.Test().ask(request, run, int(index))
