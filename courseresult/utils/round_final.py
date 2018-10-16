# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def round_final(final):
    fstr = repr(final)
    signif_digits, fract_digits = fstr.split('.')
    signif_lastdigit = int(signif_digits[-1])
    fract_lastdigit = int(fract_digits[0])
    j = 0.00
    k = 0.00
    if signif_lastdigit == 9:
        j = 1.00
    if fract_lastdigit == 5:
        k = 1.00
        final -= 0.5
    final = float(final + j + k)
    return final
