
import os
from pathlib import Path

def get_modelpath(envid):
    """
    to create a path to save the data from the network that we will analize.
    """
    # Make a local file directories
    path = Path('.') / 'files'
    os.makedirs(path, exist_ok=True)
    path = path / envid
    os.makedirs(path, exist_ok=True)
    
    return path