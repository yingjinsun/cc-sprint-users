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

def getAllUsers(request):
    user_list_json = serializers.serialize("json", UsersServiceImple().getAllUsers())
    response = Response().success(user_list_json)
    return HttpResponse(json.dumps(response), content_type="application/json")

def getCertainUser(request, user_id):
    user_json = serializers.serialize("json", UsersServiceImple().getUserByUserId(user_id))
    response = Response().success(user_json)
    return HttpResponse(json.dumps(response), content_type="application/json")

def getAllAddresses(request):
    address_list_json = serializers.serialize("json", AddressServiceImple().getAllAddresses())
    response = Response().success(address_list_json)
    return HttpResponse(json.dumps(response), content_type="application/json")

def getCertainAddress(request, address_id):
    address_json = serializers.serialize("json", AddressServiceImple().getAllAddressByAddressId(address_id))
    response = Response().success(address_json)
    return HttpResponse(json.dumps(response), content_type="application/json")