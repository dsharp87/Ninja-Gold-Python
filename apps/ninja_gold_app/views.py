# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import datetime
import re
from django.shortcuts import render, HttpResponse, redirect

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from models import *

print "im in views"
def index(request):
    print "im indexing"
    if 'gold' not in request.session:
        print "creating variables"
        request.session['gold'] = 0
        request.session['activity_log'] = []
    return render(request, 'ninja_gold_app/index.html')

def process(request):
    print "im processing"
    if request.POST['activity'] == "52":
        result = random.randrange(10, 21)
        request.session["gold"] += result
        string = "You visited the farm and earned {} gold on {}.".format(result, datetime.datetime.now().strftime("%y/%m/%d, %I:%M:%S%p"))
        style = "green"
        response = (string, style)
        request.session['activity_log'].insert(0, response)
        return redirect('/ninja_gold_app')
    if request.POST['activity'] == "105":
        result = random.randrange(5, 11)
        request.session["gold"] += result
        string = "You explored the cave and found {} gold on {}.".format(result, datetime.datetime.now().strftime("%y/%m/%d, %I:%M:%S%p"))
        style = "green"
        response = (string, style)
        request.session['activity_log'].insert(0, response)
        return redirect('/ninja_gold_app')
    if request.POST['activity'] == "7":
        result = random.randrange(2, 6)
        request.session["gold"] += result
        string = "You knocked on a door and got {} gold thrown at you on {}.".format(result, datetime.datetime.now().strftime("%y/%m/%d, %I:%M:%S%p"))
        style = "green"
        response = (string, style)
        request.session['activity_log'].insert(0, response)
        return redirect('/ninja_gold_app')
    if request.POST['activity'] == "99":
        result = random.randrange(-50, 51)
        request.session["gold"] += result
        if result > -1:
            string = "You went to the casino and won {} gold on {}.".format(result, datetime.datetime.now().strftime("%y/%m/%d, %I:%M:%S%p"))
            style = "green"
            response = (string, style)
            request.session['activity_log'].insert(0, response)
        else:
            string = "You went to the casino and lost {} gold on {}.YOU'RE A LOSER".format(result, datetime.datetime.now().strftime("%y/%m/%d, %I:%M:%S%p"))
            style = "red"
            response = (string, style)
            request.session['activity_log'].insert(0, response)
            return redirect('/ninja_gold_app')
    return redirect('/ninja_gold_app')


def reset(request):
    print "im reseting"
    for key in request.session.keys():
        del request.session[key]
    return redirect('/ninja_gold_app')
