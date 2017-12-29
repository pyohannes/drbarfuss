from django.shortcuts import render

import enquirer.models
from ._simpletest import SimpleTest


NAME = 'ADS-L Light'
DESCRIPTION = "Kurzform für interne Testzwecke."


class Test(SimpleTest):

    QUESTIONS = (
        ('Bitte wählen Sie zu den nun folgenden Fragen eine Antwort aus und '\
         'klicken Sie auf "Weiter", um zur nächsten Frage zu gelangen.\n\n' \
         'Um zu beginnen, wählen Sie bitte die unten vorgegebene '\
         'Antwortmöglichkeit "Ich habe verstanden" und klicken Sie auf '\
         '"Weiter".',),
        ("haben mich Dinge beunruhigt, die mir sonst nichts ausmachen.", 0, 1, 2, 3),
        ("war alles anstrengend für mich.", 0, 1, 2, 3),
        ("waren die Leute unfreundlich zu mir.", 0, 1, 2, 3),
        ("hatte ich das Gefühl, dass mich die Leute nicht leiden können.", 0, 1, 2, 3),
        ('Die Befragung ist nun abgeschlossen. Sie können dieses '\
         'Browserfenster schließen.',),
    )

    ANSWERS = ('selten', 'manchmal', 'öfters', 'meistens')

    PREFIX = "Während der letzten Woche ...\n\n"

    def setup(self):
        t = enquirer.models.Test(
                module=__name__,
                name=NAME,
                description=DESCRIPTION,
                needs_sex=True,
                needs_birth=False)
        t.save()

    def evaluate(self, request, run):
        ctx = {
            'run' : run, 
            'txt_title' : 'Auswertung %s' % run.test.name,
        }

        return render(request, '%s.html' % run.test.module, ctx)
