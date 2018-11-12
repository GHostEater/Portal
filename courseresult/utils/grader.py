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

    # if (total >= 70.00) and (total <= 100.00):
    #     grade = 'A'
    #     gp = 5
    # elif (total >= 60.00) and (total <= 69.00):
    #     grade = 'B'
    #     gp = 4
    # elif (total >= 50.00) and (total <= 59.00):
    #     grade = 'C'
    #     gp = 3
    # elif (total >= 45.00) and (total <= 49.00):
    #     grade = 'D'
    #     gp = 2
    # elif (total >= 40.00) and (total <= 44.00):
    #     grade = 'E'
    #     gp = 1
    # elif total <= 39.00:
    #     grade = 'F'
    #     gp = 0
    #
    # if grade == 'F':
    #     status = 0
    # else:
    #     status = 1

    data = {
        "grade": g,
        'gp': gp,
        'status': status
    }
    return data
