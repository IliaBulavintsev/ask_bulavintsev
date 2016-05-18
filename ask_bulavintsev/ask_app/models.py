from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils.timezone import now
from django.db.models import Count

# Create your models here.


class QuetionManager(models.Manager):
    def by_likes(self):
        return sorted(self.all(), key=lambda q: q.get_rating(), reverse=True)

    def by_hot(self):
        return self.order_by('-rating')

    def by_tag(self, tag):
        return self.filter(tags=tag).order_by('-datetime')

    def by_date(self):
        return self.order_by('-datetime')


class Profile(models.Model):
    avatar = models.FileField()
    user = models.OneToOneField(User, related_name='profile')


class Tag(models.Model):
    text = models.CharField(max_length=32)

    def get_absolute_url(self):
        return '/tag/{0}/'.format(self.id)


class Quetion(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=4096)
    question_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    datetime = models.DateTimeField(default=now)
    tags = models.ManyToManyField(Tag, related_name='questions')
    objects = models.Manager()
    manager = QuetionManager()
    rating = models.IntegerField(blank=True, default=0)

    def get_absolute_url(self):
        return '/question/{0}/'.format(self.id)

    def get_tags(self, tags):
        list_tags = tags.split(",")
        for tag in list_tags:
            tg = Tag.objects.filter(text=tag)
            if tg:
                self.tags.add(tg)
            else:
                tg = Tag(text=tag)
                tg.save()
                self.tags.add(tg)


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Quetion, related_name='answers')
    text = models.CharField(max_length=2048)
    is_correct = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=now)


# class Rating(models.Model):
#     user = models.ForeignKey(User)
#     rating_question = models.ForeignKey(Quetion)
#     is_like = models.BooleanField()



class HotMixin(models.Model):
    def get_rating(self):
        answers = self.annotate(Count('answers'))
        return answers