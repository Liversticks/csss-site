from django.shortcuts import render

from csss.views_helper import create_main_context

TAB = 'events'


def mm2019(request):
    return render(request, 'events/mm/2019/mountain_madness2019.html', create_main_context(request, TAB))


def mm2020(request):
    return render(request, 'events/mm/2020/mountain_madness2020.html', create_main_context(request, TAB))


def mm2021(request):
    return render(request, 'events/mm/2021/mountain_madness2021.html', create_main_context(request, TAB))
