
from datetime import datetime as dt

class AddressLabelConfigFields:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class SubCategory:
    """
    SubCategory Model
    """

    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "fields":
                        if isinstance(value, list):
                            value = [AddressLabelConfigFields(item) for item in value]
                        else:
                            value = list(AddressLabelConfigFields(value))
                self.__attributes.append(key)
                setattr(self, key, value)

class Fields:
    """
    Fields Model
    """

    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "sub_categories":
                        if isinstance(value, list):
                            value = [SubCategory(item) for item in value]
                        else:
                            value = list(SubCategory(value))
                self.__attributes.append(key)
                setattr(self, key, value)

class InsuranceProviderConfigs:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None

                self.__attributes.append(key)
                setattr(self, key, value)

class AddressLabelConfig:
    """
    Address Label Configuration Model
    """

    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "fields":
                        if isinstance(value, list):
                            value = [Fields(item) for item in value]
                        else:
                            value = list(Fields(value))
                    if key == "created_at" or key == "updated_at":
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                    if key == "address_label_config_customization_ids":
                        value = list(value)
                    
                    if key == "insurance_provider_configs":
                        if isinstance(value, list):
                            value = [InsuranceProviderConfigs(item) for item in value]
                        else:
                            value = list(InsuranceProviderConfigs(value))
                    if key == "public_boolean_fields" or key == "public_list_fields":
                        if isinstance(value, list):
                            value = list(value)
                        else:
                            value = list(value)
                    if key == "archived":
                        value = bool(value)
                self.__attributes.append(key)
                setattr(self, key, value)

    def __repr__(self):
        return f"AddressLabelConfig(label_type={self.label_type}, label_size={self.label_size})"