from infos.models import Address
from django.forms import model_to_dict
from infos.models import User
from infos.services.ValidationService import ValidationServiceImple


class AddressServiceImple(object):
    def getAllAddresses(self):
        addresses = list(map(lambda x: model_to_dict(x),Address.objects.all()))
        return addresses

    def addAddress(self, request):
        addressNo = request.get('address_no')
        streetName1 = request.get('street_name_1')
        streetName2 = request.get('street_name_2')
        city = request.get('city')
        region = request.get('region')
        countryCode = request.get('country_code')
        postalCode = request.get('postal_code')
        validResult = ValidationServiceImple().validAddress(addressNo,streetName1,streetName2, city, region, countryCode, postalCode)
        print(validResult)
        new_address = Address(addressNo=addressNo,
                        streetName1=streetName1,
                        streetName2=streetName2,
                        city=city,
                        region=region,
                        countryCode=countryCode,
                        postalCode=postalCode,
                        userId_fk=User.objects.get(userID=request.get('user_id_fk'))
                        )
        new_address.save()
        return "Success!"

    def updateAddress(self, request, address_id):
        address = Address.objects.get(addressID=address_id)
        address.addressNo = request.get('address_no')
        address.streetName1 = request.get('street_name_1')
        address.streetName2 = request.get('street_name_2')
        address.city = request.get('city')
        address.region = request.get('region')
        address.countryCode = request.get('country_code')
        address.postalCode = request.get('postal_code')
        address.userId_fk = User.objects.get(userID=request.get('user_id_fk'))
        address.save()
        return "Success!"

    def deleteAddress(self, address_id):
        Address.objects.get(addressID=address_id).delete()
        return "Success!"

    def getAddressByAddressId(self, address_id):
        address = Address.objects.filter(addressID=address_id)
        address = list(map(lambda x: model_to_dict(x), address))
        return address