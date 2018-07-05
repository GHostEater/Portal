# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def grader(total):
    grade = ''
    gp = 0
    if (total >= 70) and (total <= 100):
        grade = 'A'
        gp = 4
    elif (total >= 60) and (total <= 69):
        grade = 'B'
        gp = 3
    elif (total >= 50) and (total <= 59):
        grade = 'C'
        gp = 2
    elif (total >= 45) and (total < 50):
        grade = 'D'
        gp = 1
    elif total <= 44:
        grade = 'E'
        gp = 0

    if grade == 'E':
        status = 0
    else:
        status = 1

    data = {
        "grade": grade,
        'gp': gp,
        'status': status
    }
    return data
