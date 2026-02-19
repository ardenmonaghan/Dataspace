import os
import duckdb
import uuid
from pathlib import Path
import logging
from sqlalchemy import (
    create_engine, Column, String, DateTime, Integer, Text
)
from .db_constants import DATA_ROOT
from fastapi import UploadFile



# from constants import Dataset

def detect_upload_type(filename: str):
    '''
    detect_upload_type is a function that detects the type of the file that is being uploaded.

    Args: filename: str - The name of the file that is being uploaded.

    Returns: 
        str - The type of the file that is being uploaded.
    '''
    extension = Path(filename).suffix.lower()

    if extension == ".csv":
        return "csv"
    elif extension == ".json":
        return "json"
    elif extension == ".jsonl":
        return "jsonl"
    elif extension == ".sqlite":
        return "sqlite"
    elif extension == ".sql_dump":
        return "sql_dump"
    else:
        return "unknown"

def save_raw_file(dataset_dir: Path, file: UploadFile) -> Path:
    '''
    save_raw_file is a function that saves the raw file to the dataset directory.

    Args:
        dataset_dir: Path - The directory to save the raw file to. (Must Exist)
        file: UploadFile - The file to save.

    Returns:
        Path - The path to the saved raw file.
        int - The size of the saved raw file.
    '''

    if not dataset_dir.exists():
        raise FileNotFoundError(f"Dataset directory {dataset_dir} does not exist.")

    raw_saving_path = dataset_dir / f"raw_{file.filename}"
    size = 0

    with open(raw_saving_path, "wb") as f:
        while True:
            # Read 1MB at a time.
            chunk = file.file.read(1024 * 1024)

            # If no chunk break the loop.
            if not chunk:
                break

            f.write(chunk)
            size += len(chunk)

    return raw_saving_path, size

if __name__ == "__main__":
    print(detect_upload_type("test.csv"))
    
# running python3 db_helpers/db_services.py 
