import pytest
import os
from main import filter_lines

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w') as f:
        f.write("line1\nline2\nkeyword\nline3\n")
    return file_path

@pytest.fixture(autouse=True)
def cleanup():
    yield
    if os.path.exists('filtered.txt'):
        os.remove('filtered.txt')

@pytest.mark.parametrize("keyword, expected_lines", [
    ("keyword", ["keyword\n"]),
    ("line", ["line1\n", "line2\n", "line3\n"]),
    ("missing", []),
])
def test_filter_lines(temp_file, keyword, expected_lines):
    filter_lines(temp_file, keyword)
    with open('filtered.txt', 'r') as outfile:
        result = outfile.readlines()
    assert result == expected_lines