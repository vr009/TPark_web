from django.shortcuts import render
from .models import Profile, Question, Tag, Like, Answer

OBJ_NUM = 5

def paginate(object_list, signed_up:bool, request, per_page=5):
    pass



# список новых вопросов
def index(request):
    questions = Question.objects.new(OBJ_NUM)
    return render(request, 'index.html', {'questions': questions, 'signed_up': True})

#список горячих вопросов
def hot(request):
    questions = Question.objects.hot(OBJ_NUM)
    return render(request, 'hot.html', {'questions': questions, 'signed_up': False})

#список вопросов по тегу
def onetag(request, tag):
    questions = Question.objects.by_tag(tag)
    return render(request, 'onetag.html', {'questions': questions , 'signed_up': True})


def ask(request):
    return render(request, 'ask.html', {'signed_up': True})

def login(request):
    return render(request, 'login.html', {'signed_up': True})

def settings(request):
    return render(request, 'settings.html', {'signed_up': True})

def signup(request):
    return render(request, 'signup.html', {'signed_up': False})

def tagpage(request):
    return render(request, 'tagpage.html', {'signed_up': False})

def one_question(request, pk: int):
    question = Question.objects.get(id=pk)
    answers = Answer.objects.by_question(pk)
    return render(request, 'question.html', {"question": question, "answers": answers, 'signed_up': True})