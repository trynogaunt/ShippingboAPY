from api_wrapper import APIWrapper

class Addresses(APIWrapper):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.endpoint = 'addresses'
    
    def get_addresses(self):
        return self.get(f"{self.endpoint}?limit=2")
    
    def address(self, adress_id):
        return self.get(f"{self.endpoint}/{adress_id}")
    
    def create_address(self, apartement_number : int, building : str, city : str, civility : str, company_name : str, country : str, email : str, eori_importer : str,\
                    firstname : str, fullname : str, instructions : str, lastname : str, phone1 : str, phone2 : str, place_name : str, state : str | None ,\
                    street1 : str, street2 : str | None, street3 : str | None, street4 : str | None, vat_importer : str, zip : str):
        if country is None:
            raise ValueError("Country is required")
        
        data = {
            "apartement_number": apartement_number,
            "building": building,
            "city": city,
            "civility": civility,
            "company_name": company_name,
            "country": country,
            "email": email,
            "eori_importer": eori_importer,
            "firstname": firstname,
            "fullname": fullname,
            "instructions": instructions,
            "lastname": lastname,
            "phone1": phone1,
            "phone2": phone2,
            "place_name": place_name,
            "state": state,
            "street1": street1,
            "street2": street2,
            "street3": street3,
            "street4": street4,
            "vat_importer": vat_importer,
            "zip": zip
        }
        try:
            return self.post(self.endpoint, data)
        except Exception as e:
            print(f"Can't create adress: {e}")
            return None
        
    def update_address(self, adress_id, data):
        return self.put(f"{self.endpoint}/{adress_id}", data)