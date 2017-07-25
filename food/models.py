from django.db import models
from member.models import Member

class Store(models.Model):
    name = models.CharField(max_length=10, default='店家名稱')
    phone = models.CharField(max_length=10, default='')
    note = models.CharField(max_length=100, blank=True, default='店家備註')

    def __str__(self):
        return self.name

class Food(models.Model):
    store = models.ForeignKey('Store', related_name='menu')
    name = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateField()
    member = models.ForeignKey(Member, related_name='order')
    store = models.ForeignKey(Store)
    food = models.ForeignKey(Food)
    rank = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return '[{o.date}] {o.member}: {o.store}-{o.food}'.format(self)
