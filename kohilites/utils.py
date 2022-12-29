import pathlib

from typing import Union


def _convert_str_to_pathlib_path(path: Union[pathlib.Path, str]) -> pathlib.Path:
    """Converts a path written as a string to pathlib format"""
    return pathlib.Path(path) if type(path) is str else path


def make_path_if_not_exist(path: Union[pathlib.Path, str]):
    """Check if path exists, if it does not exist then create it"""
    path = _convert_str_to_pathlib_path(path)
    if not path.exists():
        path.mkdir(parents=True)