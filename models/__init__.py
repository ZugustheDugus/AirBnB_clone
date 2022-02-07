from . import base_model
from .engine.file_storage import FileStorage
from . import user

all = [base_model.BaseModel, user.User]

storage = FileStorage()
storage.reload()