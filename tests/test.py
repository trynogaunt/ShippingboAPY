def update_product(asin = None, cdiscount_price = None, client_ref = None, eco_tax_cents = None, hs_code = None, is_pack = None, location = None,\
                    parent_source = None, parent_source_ref = None, physical_stock = None, picture_url = None, source = None, source_ref = None, supplier = None , user_ref = None , weight = None , width = None, height = None , lengh = None, title = None):
    for key, value in locals().items():
        print(f"{key} = {value}")


update_product()