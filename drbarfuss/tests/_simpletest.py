import datetime
from django.shortcuts import render
from interview.models import Answer


class SimpleTest(object):

    QUESTIONS = tuple()

    ANSWERS = tuple()

    PREFIX = ""

    def setup(self):
        pass

    def ask(self, request, run, index=0):
        ctx = {
                'run': run,
                'question_next' : str(index + 1),
                'progress' : str(100 * (index + 1) / len(self.QUESTIONS)),
        }

        choices = [ tuple(), tuple() ]

        if index > 1:
            self._store_answer(request, run, index)

        if index == 0:
            ctx['question'] = self.QUESTIONS[0][0]
            choices = [ ('Ich habe verstanden',), (0,) ]
        elif index >= (len(self.QUESTIONS) - 1):
            ctx['question'] = self.QUESTIONS[-1][0]
            self._finish_run(run)
        else:
            ctx['question'] = self.PREFIX + self.QUESTIONS[index][0]
            choices = [ self.ANSWERS, self.QUESTIONS[index][1:] ]

        ctx['choices'] = self._make_choices(*choices)

        return render(request, 'question.html', ctx)

    def _make_choices(self, texts, values):
        return [ dict(text=text, index=index, value=value) \
                 for index, (text, value) in enumerate(zip(texts, values)) ]

    def _store_answer(self, request, run, index):
        # delete existing answers
        for answer in Answer.objects.filter(run=run, index=index):
            answer.delete()
        Answer(
                run=run, 
                index=index, 
                value=int(request.POST['choice'][0])).save()

    def _finish_run(self, run):
        run.finished = datetime.date.today()
        run.save()
