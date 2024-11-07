import os
import json
import pytest
from utils.file import (
    generate_ndjson_from_docs_folder,
    ensure_path_exists,
)
from pathlib import Path


def test_generate_ndjson_from_docs_folder():
    input_folder = Path("./utils/_test_input")
    output_file = input_folder / "output.ndjson"

    # Create sample JSON files
    (input_folder / "file1.json").write_text(json.dumps({"key1": "value1"}))
    (input_folder / "file2.json").write_text(json.dumps({"key2": "value2"}))

    generate_ndjson_from_docs_folder(str(input_folder), str(output_file))

    with open(output_file, 'r') as f:
        lines = f.readlines()
        print(lines)
        print(json.loads(lines[0]))
        assert len(lines) == 2
        assert json.loads(lines[0])["key2"] ==  "value2"
        assert json.loads(lines[1])["key1"] ==  "value1"

def test_ensure_path_exists():
    input_folder = Path("./utils/_test_input")


    test_folder = "test_new_dir"

    path = input_folder / test_folder / "file.txt"
    path = input_folder / test_folder / "file.txt"
    ensure_path_exists(str(path))
    assert not os.path.exists(path)
    assert os.path.exists(input_folder / test_folder)

# def test_create_doc_from_file():
#     def mock_transform(content):
#         return f"{{\"transformed\": {content}}}"

#     def mock_create_doc_filename(content):
#         return "test_doc", "test_component"
    
#     input_folder = Path("./utils/_test_input")

#     file_path = input_folder / "test.txt"
#     file_path.write_text("{\"res\": \"This is a test file.\"}", encoding='utf-8')
#     print(str(file_path))
#     _create_doc_from_file(str(file_path), mock_transform, mock_create_doc_filename)

#     output_path =  Path("./_docs") / "test_component" / "test_doc.json"
#     # assert os.path.exists(output_path)
#     with open(output_path, 'r') as f:
#         content = json.load(f)
#         assert content == {"transformed": {"res": "This is a test file."}}

# def test_process_files(tmp_path):
#     def mock_transform(content):

#         return {"transformed": content}

#     def mock_create_doc_filename(content):
#         return "doc", "component"

#     folder_path = tmp_path / "input"
#     folder_path.mkdir()
#     (folder_path / "file1.txt").write_text("File 1 content")
#     (folder_path / "file2.txt").write_text("File 2 content")

#     process_files(str(folder_path), mock_transform, mock_create_doc_filename)

#     output_path1 = tmp_path / "_docs" / "component" / "doc.json"
#     output_path2 = tmp_path / "_docs" / "component" / "doc.json"
#     assert os.path.exists(output_path1)
#     assert os.path.exists(output_path2)

if __name__ == '__main__':
    pytest.main()