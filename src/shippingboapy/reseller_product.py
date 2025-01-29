from api_wrapper import APIWrapper

class ResellerProducts(APIWrapper):
    def __init__(self, headers):
        super().__init__(headers)
        self.endpoint = 'reseller_products'

    def get_reseller_products(self):
        return self.get(self.endpoint)
    
    def reseller_product(self, reseller_product_id):
        return self.get(f"{self.endpoint}/{reseller_product_id}")