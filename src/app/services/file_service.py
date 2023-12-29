from pathlib import Path
from typing import List

from app.core.errors import MoveFilesError


def show_files(path: str) -> List[str]:
    dir_list = []
    for item in Path(path).iterdir():
        if item.is_file():
            dir_list.append(item.name)

    return dir_list

def show_files_with_suffix(path: str, suffix: str) -> List[str]:
    dir_list = []
    for item in Path(path).iterdir():
        if item.is_file() and item.suffix == suffix:
            dir_list.append(item.name)

    return dir_list


def move_files_to_new_folder(path:str, new_folder:str, suffix:str):
    try:
        new_folder_path = Path(new_folder)
        new_folder_path.mkdir(parents=True, exist_ok=True)
        
        for item in Path(path).iterdir():
            if item.is_file() and item.suffix == suffix:
                new_path = new_folder_path / item.name
                item.rename(new_path)
            
    except Exception as e:
        raise MoveFilesError(f"Fehler beim Verschieben der Dateien: {e}")
    
    
