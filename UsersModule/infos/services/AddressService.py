from infos.models import Address
class AddressServiceImple(object):
    def getAllAddresses(self):
        addresses = Address.objects.all()
        return addresses

    def getAllAddressByAddressId(self, address_id):
        address = Address.objects.filter(addressID=address_id)
        return address