class ResourceNotFoundException(Exception):
    def __init__(self, message, resource_id):
        self.message = message
        self.resource_id = resource_id


class BadRequestException(Exception):
    def __init__(self, message):
        self.message = message


class UnauthorizedException(Exception):
    def __int__(self):
        self.message = "The user is not allowed to access this server"
