from django.db import models
from django.core.cache import cache


class UserManager(models.Manager):
    def get_user(self, login):
        try:
            return self.get(login=login)
        except self.DoesNotExist:
            return None


class QuestionManager(models.Manager):
    def hot(self):
        return self.order_by('-rating')[:100]

    def new(self):
        return self.order_by('-date')[:100]

    def by_tag(self, tag):
        return self.filter(tags__name__iexact=tag).order_by('-rating')[:100]


class AnswerManager(models.Manager):
    def by_question(self, quest_id: int):
        return self.filter(question=quest_id).all()



class TagManager(models.Manager):
    def add_qst(self, tag_str, question):
        tag, created = self.get_or_create(name=tag_str)
        question.tags.add(tag)
        return tag

    def by_tag(self, tag_str):
        return self.filter(title=tag_str).first().questions.all()

    def popular(self):
        return cache.get('test')

class LikeQManager(models.Manager):
    def like_count(self,questions):
        for question in questions:
            question.rating = self.filter(id_question=question).count()
        return questions