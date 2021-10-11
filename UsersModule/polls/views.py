from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from ResponseUtil import Response
from polls.models import Question


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # resp = {'errorcode': 100, 'detail': 'Get success'}
    resp = Response().success("test")
    return HttpResponse(json.dumps(resp), content_type="application/json")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)