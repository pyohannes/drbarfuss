import enquirer.models
from ._simpletest import SimpleTest


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

    def setup(self):
        t = enquirer.models.Test(
                module=__name__,
                name=NAME,
                description=DESCRIPTION,
                needs_sex=True,
                needs_birth=False)
        t.save()
