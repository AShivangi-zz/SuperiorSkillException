from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

"""Each view is responsible for doing one of two things: returning an HttpResponse object containing 
the content for the requested page, or raising an exception such as Http404. The rest is up to you."""

"""Your view can read records from a database, or not. 
It can use a template system such as Django’s – or a third-party
 Python template system – or not. It can generate a PDF file, 
 output XML, create a ZIP file on the fly, anything you want, 
 using whatever Python libraries you want."""



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        """
        request.POST is a dictionary-like object that lets you access submitted data by key name. 
        In this case, request.POST['choice'] returns the ID of the selected choice, as a string. 
        request.POST values are always strings.
        
        request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data.
         The above code checks for KeyError and redisplays the question form with an error message 
         if choice isn’t given.
        """
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
        """
        After incrementing the choice count, the code returns an HttpResponseRedirect rather than a
         normal HttpResponse. HttpResponseRedirect takes a single argument:
          the URL to which the user will be redirected 
          (see the following point for how we construct the URL in this case).

        As the Python comment above points out, you should always return an HttpResponseRedirect 
        after successfully dealing with POST data. This tip isn’t specific to Django; 
        it’s just good Web development practice.
        """

        """
        We are using the reverse() function in the HttpResponseRedirect constructor in this example.
         This function helps avoid having to hardcode a URL in the view function. 
        It is given the name of the view that we want to pass control to and the variable portion 
        of the URL pattern that points to that view. In this case, using the URLconf we set up in Tutorial 3,
         this reverse() call will return a string like

        '/polls/3/results/'
        where the 3 is the value of question.id. This redirected URL will then call the 
        'results' view to display the final page.
        """
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))