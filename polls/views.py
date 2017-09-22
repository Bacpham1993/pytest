#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import datetime, time
from .greeter import greeting_at
import pytest
from mysite.factory import PersonFactory


@pytest.fixture
def person():
	return PersonFactory.build()
	
@pytest.fixture
def person_in_db(db):
	return PersonFactory.create()
	

def greet(request):
	"""
	now = datetime.now().time()
	if time(5) < now < time(12):
		greeting = 'morning'
	elif time(18) < now < time(21):
		greeting = 'evening'
	else:
		greeting = 'day'
	return HttpResponse('Good %s' % greeting)
	"""	
	now = datetime.now().time()
	greeting = greeting_at(now)		
	return HttpResponse('Good %s' % greeting)
	
def test_foo(settings):
	settings.DATE_FORMAT = 'Y-m-d'
def test_with_client(client):
	response = client.get('/polls/')
	assert response.status_code == 200	
	
def test_hello_world(client):
	response = client.get('/polls/')
	
	assert response.status_code == 200
	assert response.content == 'Hello World!'
	
#@pytest.mark.django_db
pytestmark = pytest.mark.django_db
def test_question_count():
	assert Question.objects.count() == 0
	
@pytest.mark.django_db
def test_group_letter():
	person = PersonFactory.create(group__name = 'admins')
	assert person.group_letter() == 'A'	
	
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

	
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
		
		


