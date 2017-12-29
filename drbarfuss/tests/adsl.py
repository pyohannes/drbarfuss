import enquirer.models
from interview.models import Answer
from ._simpletest import SimpleTest
from django.shortcuts import render


NAME = 'ADS-L Allgemeine Depressionsskala'
DESCRIPTION = \
"""Die allgemeine Depressionsskala (ADS) ist ein Selbstbeurteilungsinstrument, 
mit dem die Beeinträchtigung durch depressive Symtpome innerhalb der letzten 
Woche eingeschätzt werden kann. Dabei werden sowohl emotionale, motivationale, 
kognitive, somatische als auch motorische/interaktionale Beschwerden erfragt. 
Durch ihre zeitsparende und kostengünstige Anwendbarkeit stellt die ADS ein 
sehr praktikables Verfahren dar."""


class Test(SimpleTest):

    QUESTIONS = (
        ('Bitte wählen Sie zu den nun folgenden Fragen eine Antwort aus und '\
         'klicken Sie auf "Weiter", um zur nächsten Frage zu gelangen.\n\n' \
         'Um zu beginnen, wählen Sie bitte die unten vorgegebene '\
         'Antwortmöglichkeit "Ich habe verstanden" und klicken Sie auf '\
         '"Weiter".',),
        ('haben mich Dinge beunruhigt, die mir sonst nichts ausmachen.', 0, 1, 2, 3),
        ('hatte ich kaum Appetit.', 0, 1, 2, 3),
        ('konnte ich meine trübsinnigen Launen nicht loswerden, obwohl meine Freunde/Familie versuchten, mich aufzumuntern.', 0, 1, 2, 3),
        ('kam ich mir genauso gut vor wie andere.', 3, 2, 1, 0),
        ('hatte ich Mühe, mich zu konzentrieren.', 0, 1, 2, 3),
        ('wir ich deprimiert/niedergeschlagen.', 0, 1, 2, 3),
        ('war alles anstrengend für mich.', 0, 1, 2, 3),
        ('dachte ich voller Hoffnung an die Zukunft.', 3, 2, 1, 0),
        ('dachte ich, mein Leben ist ein einziger Fehlschlag.', 0, 1, 2, 3),
        ('hatte ich Angst.', 0, 1, 2, 3),
        ('habe ich schlecht geschlafen.', 0, 1, 2, 3),
        ('war ich fröhlich gestimmt.', 3, 2, 1, 0),
        ('habe ich weniger als sonst geredet.', 0, 1, 2, 3),
        ('fühlte ich mich einsam.', 0, 1, 2, 3),
        ('waren die Leute unfreundlich zu mir.', 0, 1, 2, 3),
        ('habe ich das Leben genossen.', 3, 2, 1, 0),
        ('musste ich weinen.', 0, 1, 2, 3),
        ('war ich traurig.', 0, 1, 2, 3),
        ('hatte ich das Gefühl, dass mich die Leute nicht leiden können.', 0, 1, 2, 3),
        ('konnte ich mich zu nichts aufraffen.', 0, 1, 2, 3),
        ('Die Befragung ist nun abgeschlossen. Sie können dieses Browserfenster schließen.',),
    )

    ANSWERS = ('selten', 'manchmal', 'öfters', 'meistens')

    PREFIX = "Während der letzten Woche ...\n\n"

    NORMTABLE = (
            # Gesamt PR | Frauen PR | Manner PR | Rohwert
            (1,          3,          3,          0),
            (2,          5,          5,          1),
            (6,          9,          8.5,        2),
            (11,         15,         14,         3),
            (16,         21,         22,         4),
            (21,         25,         29,         5),
            (26,         31,         37,         6),
            (33,         38,         45,         7),
            (38,         44,         52,         8),
            (41,         49,         58,         9),
            (44,         54,         62.5,       10),
            (47,         58,         66,         11),
            (50,         61,         68.5,       12),
            (58,         65,         72.5,       13),
            (63,         68,         75,         14),
            (70,         71,         77,         15),
            (74,         74,         79,         16),
            (78,         76,         80.5,       17),
            (80,         79,         82,         18),
            (82,         80,         83,         19),
            (83,         82,         84,         20),
            (84,         83,         86,         21),
            (85,         84,         87,         22),
            (87,         86,         88,         23),
            (88,         88,         90,         24),
            (89,         89,         91,         25),
            (90,         90,         92,         26),
            (91,         91,         93,         27),
            (92,         93,         94,         28),
            (93,         94,         95,         29),
            (94,         94,         96.5,       30),
            (95,         95,         98,         31),
            (96,         96,         98,         32),
            (97,         97,         98,         33),
            (97.5,       98,         98.5,       34),
            (98,         98.5,       99,         35),
            (98.5,       99,         99,         36),
            (98.8,       99,         99,         37),
            (98.9,       99,         99,         38),
            (99,         99,         99,         39),
            (99.2,       99.5,       99.5,       40),
            (99.4,       99.5,       99.5,       41),
            (99.5,       99.5,       99.5,       42),
            (99.5,       99.6,       99.7,       43),
            (99.6,       99.6,       99.7,       44),
            (99.7,       99.7,       99.9,       45),
            (99.7,       99.7,       99.9,       46),
            (99.8,       99.8,       99.9,       47),
            (99.8,       99.8,       99.9,       48),
            (99.9,       99.8,       99.9,       49),
            (99.9,       99.8,       99.9,       50),
            (99.9,       99.8,       99.9,       51),
            (99.9,       99.8,       99.9,       52),
            (99.9,       99.9,       100,        53),
            (100,        99.9,       100,        54),
            (100,        99.9,       100,        55),
            (100,        99.9,       100,        56),
            (100,        100,        100,        57),
            (100,        100,        100,        58),
            (100,        100,        100,        59),
            (100,        100,        100,        60),
    )
             

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
            'txt_prefix' : self.PREFIX,
            'txt_title' : 'Auswertung %s' % run.test.name,
        }

        answers = list(Answer.objects.filter(run=run))[:-1]

        questions = []
        for answer in answers:
            questions.append(dict(
                txt_question=self.QUESTIONS[answer.index][0],
                txt_answer=self.ANSWERS[answer.value]))
        ctx['questions'] = questions

        rawvalue = 0
        for answer in answers:
            rawvalue += self.QUESTIONS[answer.index][1 + answer.value]
        ctx['txt_rawvalue'] = str(rawvalue)

        ctx['txt_rankvalue'] = self.NORMTABLE[rawvalue][0]
        ctx['txt_ranksexvalue'] = self.NORMTABLE[rawvalue][ 2 if run.iv_male
                else 1 ]

        return render(request, '%s.html' % run.test.module, ctx)
