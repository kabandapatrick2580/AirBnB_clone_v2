import os
from models.engine import DBStorage
from models.engine.file_storage import FileStorage

# Get the value of the environment variable HBNB_TYPE_STORAGE
storage_type = os.getenv('HBNB_TYPE_STORAGE', 'db')

# Initialize storage based on the value of HBNB_TYPE_STORAGE
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage
storage.reload()
