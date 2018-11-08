# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def cgpa_calculator(results, last, fail, outsanding):
    tnu = 0
    tcp = 0
    tce = 0
    status = 1
    gp_status = 0

    if results is not None:
        for result in results:
            tnu += float(result.course.unit)
            tcp += float(result.gp) * float(result.course.unit)

            if result.grade is not "F":
                tce += int(result.gp)

    if tcp == 0 or tnu == 0:
        gpa = 0
    else:
        gpa = tcp / tnu

    if last is not None:
        tce += float(last.tce)
        ctcp = tcp + float(last.tcp)
        ctnu = tnu + float(last.tnu)

        if ctcp == 0 or ctnu == 0:
            cgpa = 0
        else:
            cgpa = ctcp / ctnu

    else:
        ctcp = tcp
        ctnu = tnu

        if ctcp == 0 or ctnu == 0:
            cgpa = 0
        else:
            cgpa = ctcp / ctnu

    if (len(fail) > 0) or (len(outsanding) > 0):
        status = 0

    if cgpa >= 4.00:
        gp_status = 1
    if (cgpa >= 1.50) and (cgpa <= 3.99):
        gp_status = 2
    if cgpa <= 1.49:
        gp_status = 3
    if cgpa < 1.00:
        gp_status = 4

    cgpa_obj = {
        'tnu': tnu,
        'ctnu': ctnu,
        'tcp': tcp,
        'ctcp': ctcp,
        'tce': tce,
        'gpa': gpa,
        'cgpa': cgpa,
        'status': status,
        'gp_status': gp_status
    }

    return cgpa_obj
