import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from box import Box
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object
    
    Args:
    path_to_yaml (Str): Path like input
    
    Raises:
        ValueError: If the yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: A ConfigBox type
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    
    
@ensure_annotations
    
def create_directories(path_to_directories: list, verbose=True):
    """
     Create directories if they don't exist
        
    Args:
    path_to_directories (list): List of directories to be created
    ignore_log (bool, optional): ignore if multiple dirs is to be created, Defaults to False
        
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created successfully")
            
            
            
@ensure_annotations
def get_size(path: Path) -> str:
    """ get size in KB
    
    Args:
        path (Path): Path of the file
        
    Returns:
        str: Size of the file in KB
    
    """
    
    size_in_kb = round(os.path.getsize(path) / (1024))
    return f"{size_in_kb} KB"
                
                
