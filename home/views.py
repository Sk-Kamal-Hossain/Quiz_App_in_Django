from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import random

def home(request):
    return HttpResponse("Hello from kamal")

# {
#     'status' : True
#     'data' : [
#         {}
#     ]
# }

def get_quiz(requesst):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle((question_objs))

        for question_obj in question_objs:
            print(question_obj.get_answers())
            data.append({
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers()
            })
        payload = {'status' : True, 'data' : data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    
    return HttpResponse("Something goes wrong")