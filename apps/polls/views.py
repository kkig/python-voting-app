# from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
# from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)


def detail(request, question_id):
    # Shortcut for the code below
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     # Requested question_id doesn't exist
    #     raise Http404("Question does not exist.")
    # return render(request, "polls/detail.html", {"question": question})

    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
