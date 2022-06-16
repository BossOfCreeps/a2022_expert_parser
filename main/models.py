from django.db import models


class Expert(models.Model):
    name = models.CharField("Имя", max_length=1024)
    text = models.TextField("О себе")
    help = models.TextField("Чем могу помочь проектам")
    expertise = models.TextField("Экспертиза")
    competencies = models.TextField("Компетенции")
    link = models.URLField("Ссылка")
