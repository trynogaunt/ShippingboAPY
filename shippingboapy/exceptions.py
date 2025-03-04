class RequestError(Exception):
    def __init__(self, error_code, message):
        super().__init__(message, error_code)
        self.message = message
        self.error_code = error_code
    
    def __str__(self):
        return f"{self.error_code} {self.message}"