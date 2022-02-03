<<<<<<< HEAD
#!/usr/bin/python3
"""
This class stores info pertaining to reviews
Inherits from Base Model
"""


def class Review(BaseModel):
    """init the class"""
    def __init__(self, id):
=======
#!/usr/bin/python3
"""
Review class
"""

# first edit
# import statement may need editing after we work on Base Model
# from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    Public attrs
    place_id: string - empty string: will be the Place.id
    user_id: string - empty string: will be the User.id
    text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
>>>>>>> 43e9a9f80286bc46748e4610230aef121698bc5f
