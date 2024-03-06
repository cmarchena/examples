class WeatherDataUnavailableError(Exception):
    """Raised when weather data is unavailable for a requested city"""
    pass

class ServiceError(Exception):
    """Raised when a service fails"""
    pass

class EntityDoesNotExistError(Exception):
    pass


class CityNotFoundError(EntityDoesNotExistError):
    """Raised when a city cannot be found in the database"""
    pass


class WeatherDataNotFoundError(EntityDoesNotExistError):
    """Raised when a city cannot be found in the database"""
    pass