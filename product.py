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

    def update_product(self, product_id):
        return self.put(f"{self.endpoint}/{product_id}")

    def update_product_sku_ean(self, sku = None,  ean13 = None):
        url_compose = []
        if sku is None and ean13 is None:
            raise ValueError("sku or ean13 is required")
        elif sku is not None and ean13 is not None:
            raise ValueError("Can't request with both key")
        elif sku is not None and ean13 is None:
            url_compose.append("sku")
            url_compose.append(sku)
            pass
        elif ean13 is not None and sku is None:
            url_compose.append("ean13")
            url_compose.append(ean13)
            pass
        return self.put(f"{self.endpoint}/{url_compose[0]}/{url_compose[1]}", payload)