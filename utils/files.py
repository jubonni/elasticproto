import os
import json


def generate_ndjson_from_docs_folder(input_folder, output_file='combined.ndjson'):
    """
    Loop through all JSON files in a specified folder and write their contents to a single NDJSON file.

    :param input_folder: Path to the folder containing JSON files.
    :param output_file: Path to the output NDJSON file.
    """
    with open(output_file, 'w') as ndjson_file:
        for filename in os.listdir(input_folder):
            if filename.endswith('.json'):
                file_path = os.path.join(input_folder, filename)
                
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    ndjson_file.write(json.dumps(data) + '\n')

def ensure_path_exists(path):
    if os.path.splitext(path)[1]:
        dir_path = os.path.dirname(path)
    else:
        dir_path = path

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        return

def read_file_with_fallback(file_path):
    try:
        # Attempt reading with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Fallback to reading as binary and decoding manually
        with open(file_path, 'rb') as f:
            return f.read().decode('utf-8', errors='replace')  # Replace un-decodable chars

def create_doc_from_file(filepath, transform, create_doc_filemame):
    content = read_file_with_fallback(filepath)
    processed_content = transform(content)
    doc_filename, component = create_doc_filemame(content)

    output_path = f"_docs/{component}/{doc_filename}.json"
    ensure_path_exists(output_path)
    with open(output_path, 'w') as output_file:
        output_file.write(str(processed_content))

def process_files(folder_path, transform, create_doc_filemame):
    for root, _, files in os.walk(folder_path):
        for each in files:
            file_path = os.path.join(root, each)
            create_doc_from_file(file_path, transform, create_doc_filemame)


