from django.shortcuts import render
from django.http import HttpResponse
import json
from ResponseUtil import Response
from infos.services.UsersService import UsersServiceImple
from infos.services.AddressService import AddressServiceImple
from ConstantUtil import Constant
import requests

from django.core import serializers
def index(request):

    resp = Response().success("Connected successfully!")
    return HttpResponse(json.dumps(resp), content_type="application/json")

def users(request):
    if request.method == 'GET':
        limit = int(request.GET["limit"])
        offset = int(request.GET["offset"])
        user_list_json = UsersServiceImple().getAllUsers()
        print(user_list_json)
        user_list_json = sorted(user_list_json, key=lambda x:x["userID"])[offset: offset + limit]

        response = Response().success(user_list_json)
        result = HttpResponse(json.dumps(response), content_type="application/json")
        result['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8002'  # 设置请求头
        return result
    elif request.method == 'POST':
        requestDict = eval(request.body)
        if requestDict:
            result = UsersServiceImple().addUser(requestDict)
            response = Response().resp(Constant().POST,result) #201
            return HttpResponse(json.dumps(response), content_type="application/json")

    response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")

def certainUser(request, user_id):
    if not user_id:
        response = Response().resp(Constant().BAD_DATA, None) #400
        return HttpResponse(json.dumps(response), content_type="application/json")

    if request.method == 'GET':
        user_json = UsersServiceImple().getUserByUserId(user_id)
        if not user_json:
            response = Response().resp(Constant().NOT_FOUND, None) #404
        else:
            response = Response().success(user_json) #200
        return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'PUT':
        requestDict = eval(request.body)
        if requestDict:
            result = UsersServiceImple().updateUser(requestDict, user_id)
            response = Response().success(result)
            return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'DELETE':
        user_json = UsersServiceImple().deleteUser(user_id)
        response = Response().resp(Constant().DELETE, user_json) #204
        return HttpResponse(json.dumps(response), content_type="application/json")

    else:
        response = Response().resp(Constant().SOMETHING_WRONG, None) #422
        return HttpResponse(json.dumps(response), content_type="application/json")


def addresses(request):
    if request.method == 'GET':
        address_list_json = AddressServiceImple().getAllAddresses()
        response = Response().success(address_list_json)
        return HttpResponse(json.dumps(response), content_type="application/json")
    elif request.method == 'POST':
        requestDict = eval(request.body)
        if requestDict:
            AddressServiceImple().addAddress(requestDict)
            url = 'http://api.weatherapi.com/v1/current.json'
            params = {"key": "4bbb6a9116034b188e624454213010", "q": request.get('city'), "aqi": "no"}
            response = requests.get(url=url, params=params).text
            json_acceptable_string = response.replace("'", "\"")
            d = json.loads(json_acceptable_string)
            response = Response().success({request.get('city') + "_humidity": d["current"]["humidity"]})
            return HttpResponse(json.dumps(response), content_type="application/json")

    response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")

def certainAddress(request, address_id):
    if request.method == 'GET':
        address_json = AddressServiceImple().getAddressByAddressId(address_id)
        response = Response().success(address_json)
        return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'PUT':
        requestDict = eval(request.body)
        if requestDict:
            result = AddressServiceImple().updateAddress(requestDict, address_id)
            response = Response().success(result)
            return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'DELETE':
        address_json = AddressServiceImple().deleteAddress(address_id)
        response = Response().success(address_json)
        return HttpResponse(json.dumps(response), content_type="application/json")

    else:
        response = Response().failed()
        return HttpResponse(json.dumps(response), content_type="application/json")