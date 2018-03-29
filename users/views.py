from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('users:index'))