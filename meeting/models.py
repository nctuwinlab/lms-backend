# coding=UTF-8
from django.db import models
from member.models import Profile
import datetime


class Meeting(models.Model):
    time = models.DateTimeField(verbose_name='時間')
    location = models.CharField(max_length=20, default='', verbose_name='地點')
    speaker = models.ForeignKey(Profile, related_name='speaker',
                                verbose_name='講者')
    topic = models.CharField(max_length=255, default='', verbose_name='講題')
    file = models.URLField(verbose_name='上傳文件')

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_time = datetime.datetime.today()
        return super(Meeting, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '會議管理'
