from django.http import HttpResponse
import json
from ResponseUtil import Response
from django.conf import settings
import pickledb

db = pickledb.load('example.db', False)

def index(request):
    if request.method == 'POST':
        requestDict = eval(request.body)
        token = requestDict.get('token')
        email = requestDict.get('email')
        db.set(token, email)
        resp = Response().success("Set token Successfully!")
        return HttpResponse(json.dumps(resp), content_type="application/json")
    elif request.method == "GET":
        token = request.GET["token"]
        print(token)
        res = db.get(token)
        if res:
            resp = Response().success("Successful valid!")
        else:
            resp = Response().failed()
        return HttpResponse(json.dumps(resp), content_type="application/json")




