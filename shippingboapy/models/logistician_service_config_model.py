from datetime import datetime

class Config:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)


class LogisticianServiceConfig:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "config":
                        if isinstance(value, dict):
                            value = Config(value)
                    if key =="created_at" or key == "updated_at":
                        value = datetime.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                    if key == "archived":
                        value = bool(value)
                self.__attributes.append(key)
                setattr(self, key, value)
