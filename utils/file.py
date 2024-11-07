import os
import json


def generate_ndjson_from_docs_folder(input_folder: str, output_file: str='combined.ndjson'):
    """
    Generates a newline-delimited JSON (NDJSON) file from all JSON files in a specified folder.
    Args:
        input_folder (str): The path to the folder containing JSON files.
        output_file (str, optional): The path to the output NDJSON file. Defaults to 'combined.ndjson'.
    Raises:
        FileNotFoundError: If the input folder does not exist.
        IOError: If there is an error reading a JSON file or writing to the NDJSON file.
    Example:
        generate_ndjson_from_docs_folder('/path/to/json/folder', 'output.ndjson')
    """

    with open(output_file, 'w') as ndjson_file:
        for filename in os.listdir(input_folder):

            if not filename.endswith('.json'):
                print(f"warning: {filename} filetype not supported, only .json")
                continue

            file_path = os.path.join(input_folder, filename)

            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                ndjson_file.write(json.dumps(data) + '\n')
            
def ensure_path_exists(path):
    """
    Ensures that the directory for the given path exists. If the path includes a file name, 
    the function will create the directory containing the file. If the path is a directory, 
    it will create the directory itself.
    Args:
        path (str): The file or directory path to check and create if it does not exist.
    Returns:
        None
    """
    if os.path.splitext(path)[1]:
        dir_path = os.path.dirname(path)
    else:
        dir_path = path

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        return

def read_file_with_fallback(file_path: str):
    """
    Reads the content of a file with a fallback mechanism for encoding issues.
    This function attempts to read the file at the given file path using UTF-8 encoding.
    If a UnicodeDecodeError occurs, it falls back to reading the file in binary mode and
    then decodes it using UTF-8 with replacement for any decoding errors.
    Args:
        file_path (str): The path to the file to be read.
    Returns:
        str: The content of the file as a string. If there are any undecodable bytes,
             they will be replaced with the Unicode replacement character.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'rb') as f:
            return f.read().decode('utf-8', errors='replace')

