import shutil
from pathlib import Path
import pytest

from kohilites.utils import (
    _convert_str_to_pathlib_path,
    make_path_if_not_exist
)


@pytest.fixture
def test_output_path():
    """Generates pathlib.Path to dump intermediate test data.
    Yields:
        Output path to dump intermetiate test data.
    """
    test_output_path = _convert_str_to_pathlib_path("tests/temp/")
    make_path_if_not_exist(test_output_path)
    yield test_output_path
    shutil.rmtree("tests/temp/")


def test_convert_str_to_pathlib_path(test_output_path: Path):
    """Tests that file_ops method convert_str_to_pathlib_path.
        returns type patlib.Path.
    Args:
        test_output_path (pathlib.Path): output path to dump intermetiate test data
    """
    assert isinstance(test_output_path, Path)


def test_path_exists(test_output_path: Path):
    """Tests that the path generated by file_ops method
        make_path_if_not_exist exists.
    Args:
        test_output_path (pathlib.Path): Output path to dump intermetiate test data.
    """
    assert test_output_path.exists()