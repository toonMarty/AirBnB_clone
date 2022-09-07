"""
This module contains a call to the method reload
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
