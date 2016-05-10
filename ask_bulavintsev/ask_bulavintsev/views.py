from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from ask_app.models import *
from django.db.models import Count

# def wsgi(request):
# 	if request.method == "GET":
# 		params = create_params(request.GET.lists())
# 	elif request.method == "POST":
# 		params = create_params(request.POST.lists())
# 	return HttpResponse('<h3>{}</h3><p>{}<p>'.format(request.method, params))
#
#
# def create_params(params):
# 	get_params = {}
# 	for (key, values) in params:
# 		get_params[key] = values
# 	return get_params


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(objects, page):
    paginator = Paginator(objects, 10)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects


def index(request):
    questions_by_date = Quetion.manager.by_date().annotate(Count('answers'))
    questions = paginate(questions_by_date, request.GET.get('page'))
    return render(request, 'index.html', {'questions': questions, 'flag': 1})


def hot(request):
    question_hot = Quetion.manager.by_hot().annotate(Count('answers'))
    questions = paginate(question_hot, request.GET.get('page'))
    return render(request, 'index.html', {'questions': questions, 'flag': 0})


def question_detail(request, id):
    question = Quetion.objects.get(pk=id)
    return render(request, 'question.html', {'question': question})


def tag(request, id):
    tagsq = get_object_or_404(Tag, pk=id)
    question = tagsq.questions.all().annotate(Count('answers'))
    questions = paginate(question, request.GET.get('page'))
    return render(request, 'index.html', {'questions': questions})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def ask(request):
    return render(request, 'ask.html')