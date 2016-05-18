from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from ask_app.models import *
from django.db.models import Count
#from django.contrib.auth import authenticate
from django.contrib import *
from django.contrib.auth import *
from django.contrib.auth.views import *
from ask_app.forms import *
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import now


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
    if request.POST:
        response_data = {}
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                response_data['status'] = 'ok'
                return JsonResponse(response_data)
            else:
                response_data['status'] = 'bad'
                return JsonResponse(response_data)
        else:
            # the authentication system was unable to verify the username and password
            response_data['status'] = 'bad'
            return JsonResponse(response_data)
    return render(request, 'login.html')


def log_out(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')
    else:
            raise Http404


def register(request):
    if request.POST:
        form = UserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            u = User.objects.create_user(username, email, password)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'register.html', {'form': form})
    form = UserForm()
    return render(request, 'register.html', {'form': form})


def ask(request):
    if request.POST:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            title = form.cleaned_data.get('title')
            tags = form.cleaned_data.get('tags')
            quest = Quetion(title=title, text=text, question_user=request.user)
            quest.save()
            quest.get_tags(tags)
            return HttpResponseRedirect('/question/' + str(quest.pk) + '/')
        else:
            return render(request, 'ask.html', {'form': form})
    if request.user.is_authenticated():
        form = QuestionForm()
        return render(request, 'ask.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


def answer(request):
    if request.POST:
        response_data = {}
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            te = form.cleaned_data.get('text')
            quest = Quetion.objects.get(pk=int(request.POST['quest']))
            ans = Answer(user=request.user, question=quest, text=te)
            ans.save()
            response_data['status'] = 'ok'
            return JsonResponse(response_data)
        else:
            response_data['status'] = 'bad'
            return JsonResponse(response_data)
    else:
        raise Http404