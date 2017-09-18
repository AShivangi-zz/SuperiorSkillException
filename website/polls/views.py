from django.shortcuts import render
from django.template import loader

from django.shortcuts import get_object_or_404, render

from .models import Question


"""Each view is responsible for doing one of two things: returning an HttpResponse object containing 
the content for the requested page, or raising an exception such as Http404. The rest is up to you."""

"""Your view can read records from a database, or not. 
It can use a template system such as Django’s – or a third-party
 Python template system – or not. It can generate a PDF file, 
 output XML, create a ZIP file on the fly, anything you want, 
 using whatever Python libraries you want."""

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    """The render() function takes the request object as its first argument, 
    a template name as its second argument and a dictionary as its optional 
    third argument. It returns an HttpResponse object of the given template rendered with the given context."""
    return HttpResponse(template.render(context, request))

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)