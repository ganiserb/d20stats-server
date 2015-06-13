# coding=utf-8
__author__ = 'gabriel'
from django.contrib.auth.models import User
from registrator.models import Roll
from tastypie.resources import ModelResource
from tastypie import fields


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.filter(is_superuser=False)
        fields = ['username', 'first_name', 'last_name']
        allowed_methods = ['get']


class RollResource(ModelResource):
    class Meta:
        queryset = Roll.objects.all()
        player = fields.ToOneField(UserResource, 'player')
        # fields = ['roll', 'player']
        allowed_methods = ['get', 'post']