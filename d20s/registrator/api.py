# coding=utf-8
__author__ = 'gabriel'
from django.contrib.auth.models import User
from registrator.models import Roll
from tastypie.resources import ModelResource


class RollResource(ModelResource):
    class Meta:
        queryset = Roll.objects.all()


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()