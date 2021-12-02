from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup

class ValidationServiceImple(object):
    def validAddress(self, addressNo,streetName1,streetName2, city, region, countryCode, postalCode):
        """
        valid address
        """
        auth_id = "5b91521a-637e-a34b-7578-c5db463e6fa6"
        auth_token = "QEww5NZby77yZQhVKjhK"

        credentials = StaticCredentials(auth_id, auth_token)
        client = ClientBuilder(credentials).with_licenses(["us-core-cloud"]).build_us_street_api_client()

        lookup = StreetLookup()
        lookup.addressee = "Tom"
        lookup.street = streetName1
        lookup.street2 = streetName2
        lookup.city = city
        lookup.state = region
        lookup.zipcode = postalCode
        lookup.candidates = 3
        lookup.match = "invalid"  # "invalid" is the most permissive match,

        try:
            client.send_lookup(lookup)
        except exceptions.SmartyException as err:
            print(err)
            return

        result = lookup.result
        first_candidate = result[0]
        if first_candidate.components.zipcode:
            return "Valid"
        else:
            return "The address is not valid"
