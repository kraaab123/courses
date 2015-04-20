# coding: utf-8

from django.db import models

class Decan(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Specialy(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Group(models.Model):
    group_name = models.CharField(max_length=255, unique=True)
    person_number = models.IntegerField()
    decan = models.ForeignKey('Decan')
    specialty = models.ForeignKey('Specialy')
    pisun = models.OneToOneField('Pisun')

    def __unicode__(self):
        return self.group_name

class Student(models.Model):
    FLOOR_CHOICES = (
        (u'М', u'Муж'),
        (u'Ж', u'Жен'),
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    floor = models.CharField(max_length=2, choices=FLOOR_CHOICES)
    birth = models.DateField()
    group =  models.ForeignKey('Group')


class Pisun(models.Model):
    name = models.CharField(max_length=232)
    def __unicode__(self):
        return self.name


class Prepod(models.Model):
    FLOOR_CHOICES = (
        (u'М', u'Муж'),
        (u'Ж', u'Жен'),
    )
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    floor = models.CharField(max_length=2, choices=FLOOR_CHOICES)
    birth = models.DateField()