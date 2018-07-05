# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import hmac

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def hasher(request):
    data = request.data
    key = str(data['key'].decode('hex'))
    enc = str(data['enc'])

    hsh = hmac.new(key=key, msg=enc, digestmod=hashlib.sha256)
    hsh_dig = hsh.hexdigest()

    serial = {"hex": hsh_dig}

    return Response(serial)
