from api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self, base_url, api_key):
        super().__init__(base_url, api_key)
    
    def get_orders(self):
        endpoint = 'orders'
        return self.get(endpoint)
    
    def order(self, order_id):
        endpoint = f'orders/{order_id}'
        return self.get(endpoint)

    def create_order(self, billing_address_id : int, chosen_delivery_service : str, earliest_chosen_delivery_at : str[datetime] = datetime.now, earliest_delivery_at : str[datetime] =  datetime.now,\
                    earliest_shipped_at : str[datetime] = datetime.now, invoice_ref : int = 0, latest_chosen_delivery_at : str[datetime] = datetime.now, \
                    latest_delivery_at : str[datetime] = datetime, latest_shipped_at : str[datetime] = datetime.now, order_documents : list = [], order_items_attributes : list[OrderItem] = [], origin,\
                    origin_created_at, origin_ref, payment_medium, relay_ref, shipped_at, shipping_address_id, source, source_ref, state, tags_to_add,\
                    total_price_cents, total_price_currency, total_shipping_tax_cents, total_shipping_tax_currency, total_shipping_tax_included_cents,\
                    total_shipping_tax_included_currency, total_tax_cents, total_tax_currency, computed_prices, mapped_carrier, preparation_order_at, total_weight):

        endpoint = 'orders'
        order = {
            "billing_address_id": billing_address_id,
            "chosen_delivery_service": chosen_delivery_service,
            "earliest_chosen_delivery_at": earliest_chosen_delivery_at,
            "earliest_delivery_at": earliest_delivery_at,
            "earliest_shipped_at": earliest_shipped_at,
            "invoice_ref": invoice_ref,
            "latest_chosen_delivery_at": latest_chosen_delivery_at,
            "latest_delivery_at": latest_delivery_at,
            "latest_shipped_at": latest_shipped_at,
            "order_documents": order_documents,
            "order_items_attributes": order_items_attributes,
            "origin": origin,
            "origin_created_at": origin_created_at,
            "origin_ref": origin_ref,
            "payment_medium": payment_medium,
            "relay_ref": relay_ref,
            "shipped_at": shipped_at,
            "shipping_address_id": shipping_address_id,
            "source": source,
            "source_ref": source_ref,
            "state": state,
            "tags_to_add": tags_to_add,
            "total_price_cents": total_price_cents,
            "total_price_currency": total_price_currency,
            "total_shipping_tax_cents": total_shipping_tax_cents,
            "total_shipping_tax_currency": total_shipping_tax_currency,
            "total_shipping_tax_included_cents": total_shipping_tax_included_cents,
            "total_shipping_tax_included_currency": total_shipping_tax_included_currency,
            "total_tax_cents": total_tax_cents,
            "total_tax_currency": total_tax_currency,
            "computed_prices": computed_prices,
            "mapped_carrier": mapped_carrier,
            "preparation_order_at": preparation_order_at,
            "total_weight": total_weight
        }
        return self.post(endpoint, order)