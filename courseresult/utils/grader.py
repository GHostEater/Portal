# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from grade.models import Grade


def grader(total):
    grades = Grade.objects.filter(active=True)

    g = ''
    gp = ''
    status = 1

    for grade in grades:
        if(total >= grade.lower_limit) and (total <= grade.upper_limit):
            if grade.lower_limit == 0:
                status = 0
            g = grade.grade
            gp = grade.gp
            break

    data = {
        "grade": g,
        'gp': gp,
        'status': status
    }
    return data
