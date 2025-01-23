from api_wrapper import APIWrapper

class Reseller(APIWrapper):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.endpoint = 'resellers'
    
    def get_resellers(self):
        return self.get(self.endpoint)
    
    def reseller(self, reseller_id):
        return self.get(f"{self.endpoint}/{reseller_id}")