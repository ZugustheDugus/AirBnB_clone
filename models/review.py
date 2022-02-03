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