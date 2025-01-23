from api_wrapper import APIWrapper

class Product(APIWrapper):
    def __init__(self, base_url,  api_key):
        super().__init__(base_url, api_key)
        self.endpoint = 'products'
    
    def get_products(self):
        return self.get(self.endpoint)

    def product(self, product_id):

        return self.get(f"{self.endpoint}/{product_id}")
    
    def create_product(self, ean13 : str, hs_code : str , is_pack : bool , lenght : int, weight : int , width : int,  height : int, location : str, title : str,\
                    supplier : str | None , user_ref : int , product_additionnal_fields_to_add : list[dict] , picture_url : str , total_physical_stock : int):
        
        payload = {
            "ean13": ean13,
            "hs_code": hs_code,
            "is_pack": is_pack,
            "lenght": lenght,
            "weight": weight,
            "width": width,
            "height": height,
            "location": location,
            "title": title,
            "supplier": supplier,
            "user_ref": user_ref,
            "product_additionnal_fields_to_add": product_additionnal_fields_to_add,
            "picture_url": picture_url,
            "total_physical_stock": total_physical_stock
        }
        
    
        return self.post(self.endpoint, payload)

    def delete_product(self, product_id):
        return self.delete(f"{self.endpoint}/{product_id}")