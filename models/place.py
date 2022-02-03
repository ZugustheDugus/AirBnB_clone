<<<<<<< HEAD
#!/usr/bin/python3
"""
Place class, showing what a place looks like
Place inherits from Base Model
"""

class Place(BaseModel):
    """Init the class"""
    def __init__(self, id):
=======
#!/usr/bin/python3
"""
Place class
"""
# first edit
# import statement may need editing after we work on Base Model
# from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    city_id: string - empty string: will be the City.id
    user_id: string - empty string: will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list: will become list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
>>>>>>> 43e9a9f80286bc46748e4610230aef121698bc5f