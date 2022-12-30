import os
import pytest
import shutil

from kohilites import MetaData


TEST_INPUT_DIR = os.path.join("tests", "artifacts")
TEST_OUTPUT_DIR = os.path.join("tests", "temp")
TEST_INPUT_PATH = os.path.join("tests", "artifacts", "metadata.test.lua")

@pytest.fixture
def metadata_input_path_with_output():
    metadata = MetaData(TEST_INPUT_PATH, TEST_OUTPUT_DIR)
    yield metadata


@pytest.fixture
def metadata_input_path_no_output():
    metadata = MetaData(TEST_INPUT_PATH, None)
    yield metadata


@pytest.fixture
def metadata_input_dir_no_output():
    metadata = MetaData(TEST_INPUT_DIR, None)
    yield metadata


def test_input_output_input_path_with_output(metadata_input_path_with_output):
    assert metadata_input_path_with_output.input == TEST_INPUT_PATH
    assert metadata_input_path_with_output.output == TEST_OUTPUT_DIR


def test_input_output_input_path_no_output(metadata_input_path_no_output):
    assert metadata_input_path_no_output.input == TEST_INPUT_PATH
    assert metadata_input_path_no_output.output == TEST_INPUT_DIR


def test_input_output_input_dir_no_output(metadata_input_dir_no_output):
    assert metadata_input_dir_no_output.input == TEST_INPUT_DIR
    assert metadata_input_dir_no_output.output == TEST_INPUT_DIR


def test_decode_data_size(metadata_input_path_with_output):
    decoded = metadata_input_path_with_output.decode_data()
    assert len(decoded) == 71
    assert len(decoded["highlight"]) == 2


def test_decode_data_keys(metadata_input_path_with_output):
    decoded = metadata_input_path_with_output.decode_data()
    assert "highlight" in decoded
    assert "doc_props" in decoded


def test_extract_highlights_size(metadata_input_path_with_output):
    decoded = metadata_input_path_with_output.decode_data()
    highlights = list(
        metadata_input_path_with_output.extract_highlights(decoded)
    )
    assert len(highlights) == 2


def test_extract_highlights_content(metadata_input_path_with_output):
    decoded = metadata_input_path_with_output.decode_data()
    highlights = list(
        metadata_input_path_with_output.extract_highlights(decoded)
    )
    assert highlights[0]["text"] == "I got to know Fox in the summer of 1984."
    assert highlights[1]["text"] == "Fox is a cunning creature with a warm heart."


def test_extract_doc_props_content(metadata_input_path_with_output):
    decoded = metadata_input_path_with_output.decode_data()
    doc_props = metadata_input_path_with_output.extract_doc_props(decoded)
    
    assert doc_props["title"] == "Fox: A Tail"
    assert doc_props["authors"] == "Jonty Nadem, Fuzzball Korb"


def test_highlights(metadata_input_path_with_output):
    metadata_input_path_with_output.highlights()

    with open("tests/artifacts/Fox: A Tail.md", "r") as f:
        dummy_data = f.read()

    with open("tests/temp/Fox: A Tail.md", "r") as f:
        dummy_output = f.read()

    assert dummy_data == dummy_output
    shutil.rmtree("tests/temp")