from api_wrapper import ApiWrapper

class Adresses(ApiWrapper):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.endpoint = 'adresses'
    
    def get_adresses(self, limit = 10, offset = 0):
        return self.get(self.endpoint , limit = limit, offset = offset)
    
    def adress(self, adress_id):
        return self.get(f"{self.endpoint}/{adress_id}")
    
    def create_adress(self, data):
        return self.post(self.endpoint, data)
    
    def update_adress(self, adress_id, data):
        return self.put(f"{self.endpoint}/{adress_id}", data)