from django.core.management.base import BaseCommand

# Python
from random import randint

from ask_app.models import *


def create_user(start, stop):
    for x in range(start, stop, 1):
        try:
            username = 'user_'+str(x)
            first = 'first_name_'+str(x)
            last = 'last_name_'+str(x)
            password = '12345'
            img = '1.jpg'
            user = User.objects.create_user(username=username, email=None, password=password, first_name=first, last_name=last)
            user.save()
            profile = Profile(avatar=img, user=user)
            profile.save()
        except Exception as e:
            print(e)
    print('users create!')


def create_tag(start, stop):
    for x in range(start, stop, 1):
        try:
            name = 'tag_'+str(x)
            tag = Tag(text=name)
            tag.save()
        except Exception as e:
            print(e)
    print('tag create!')


def create_question(start, stop):
    users = User.objects.all()
    users_count = users.count()
    tags = Tag.objects.all()
    tags_count = tags.count()
    for x in range(start, stop, 1):
        try:
            titles = 'title_'+str(x)
            texts = 'text_'+str(x)+'  Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.'
            user = users[randint(1, users_count - 1)]
            question = Quetion(title=titles, text=texts, question_user=user)
            question.save()
            for y in range(1, 3, 1):
                question.tags.add(tags[randint(1, tags_count - 1)])
        except Exception as e:
            print(e)
    print('question create!')


def create_answer(start, stop):
    users = User.objects.all()
    users_count = users.count()
    questions = Quetion.objects.all()
    questions_count = questions.count()
    for x in range(start, stop, 1):
        try:
            texts = 'answer_text_'+str(x)
            usr = users[randint(1, users_count - 1)]
            qstn = questions[randint(1, 51)]
            answer = Answer(user=usr, question=qstn, text=texts)
            answer.save()
        except Exception as e:
            print(e)
    print('answer create!')


def create_rating(start, stop):
    users = User.objects.all()
    users_count = users.count()
    questions = Quetion.objects.all()
    for x in range(start, stop, 1):
        try:
            usr = users[randint(1, users_count - 1)]
            qst = questions[randint(1, 51)]
            rating = Rating(user=usr, question=qst, is_like=True)
            rating.save()
        except Exception as e:
            print(e)
    print('rating create!')


def create_rating_ans():
    questions = Quetion.objects.all()
    try:
        for question in questions:
            question.rating = randint(0, 101)
            question.save()
    except Exception as e:
        print(e)
    print('rating create!')



class Command(BaseCommand):
    help = 'Initialize database'

    def handle(self, *args, **options):

        #create_user(1, 101)
        #create_tag(1, 101)
        #create_question(1, 1001)
        #create_answer(1, 401)
        #create_rating(1, 1001)
        create_rating_ans()

        self.stdout.write('Successfully filled database!')