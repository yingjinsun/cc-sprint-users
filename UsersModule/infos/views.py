from django.shortcuts import render

from django.http import HttpResponse
import json
from ResponseUtil import Response
from infos.services.UsersService import UsersServiceImple
from infos.services.AddressService import AddressServiceImple

from django.core import serializers
def index(request):

    resp = Response().success("Connected successfully!")
    return HttpResponse(json.dumps(resp), content_type="application/json")

def users(request):
    if request.method == 'GET':
        user_list_json = UsersServiceImple().getAllUsers()

        response = Response().success(user_list_json)
        return HttpResponse(json.dumps(response), content_type="application/json")
    elif request.method == 'POST':
        requestDict = eval(request.body)
        if requestDict:
            result = UsersServiceImple().addUser(requestDict)
            response = Response().success(result)
            return HttpResponse(json.dumps(response), content_type="application/json")

    response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")

def getCertainUser(request, user_id):
    if request.method == 'GET':
        user_json = UsersServiceImple().getUserByUserId(user_id)
        response = Response().success(user_json)
        return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'PUT':
        requestDict = eval(request.body)
        if requestDict:
            result = UsersServiceImple().updateUser(requestDict, user_id)
            response = Response().success(result)
            return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'DELETE':
        user_json = UsersServiceImple().deleteUser(user_id)
        response = Response().success(user_json)
        return HttpResponse(json.dumps(response), content_type="application/json")

    else:
        response = Response().failed()
        return HttpResponse(json.dumps(response), content_type="application/json")


def getAllAddresses(request):
    address_list_json = serializers.serialize("json", AddressServiceImple().getAllAddresses())
    response = Response().success(address_list_json)
    return HttpResponse(json.dumps(response), content_type="application/json")

def getCertainAddress(request, address_id):
    address_json = serializers.serialize("json", AddressServiceImple().getAllAddressByAddressId(address_id))
    response = Response().success(address_json)
    return HttpResponse(json.dumps(response), content_type="application/json")