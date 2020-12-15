from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager): 
  def new(self):
    return self.order_by('-added_at')  
  def popular(self): 
    return self.order_by('-rating')



class Question(models.Model):
  objects = QuestionManager() 
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_ad = models.DateTimeField(blank = True, auto_now_add=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User, default= 'x')
  likes = models.ManyToManyField(User, related_name='likes_set')
  def __unicode__(self):
    return self.title
#  def get_absolute_url(self):
#    return '/post/%d/' % self.pk
  class Meta:
    db_table = 'questions'
    ordering = ['-added_ad']



class Answer(models.Model): 
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_ad = models.DateTimeField(blank = True, auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User, default= 'x')
  def __unicode__(self):
    return self.text
#  def get_absolute_url(self):
#    return '/post/%d/' % self.pk
  class Meta:
    db_table = 'answers'
    ordering = ['-added_ad']
