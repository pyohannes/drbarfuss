from enquirer import models


NAME = 'ADS-L Allgemeine Depressionsskala'
DESCRIPTION = \
"""Die allgemeine Depressionsskala (ADS) ist ein Selbstbeurteilungsinstrument, 
mit dem die Beeinträchtigung durch depressive Symtpome innerhalb der letzten 
Woche eingeschätzt werden kann. Dabei werden sowohl emotionale, motivationale, 
kognitive, somatische als auch motorische/interaktionale Beschwerden erfragt. 
Durch ihre zeitsparende und kostengünstige Anwendbarkeit stellt die ADS ein 
sehr praktikables Verfahren dar."""


class Test(object):
    
    def setup(self):
        t = models.Test(
                module=__name__,
                name=NAME,
                description=DESCRIPTION,
                needs_sex=True,
                needs_birth=False)
        t.save()
