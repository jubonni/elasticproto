from typing import Callable

import format_docs as fd
from collections import namedtuple
import os
from utils.file import (
    read_file_with_fallback,
    ensure_path_exists,
)


Document = namedtuple("Document", ["title", "type"])

def define_api_spec_document(content):
    return Document(
        fd.create_api_spec_title(content), 
        "api-spec",
    )

def define_guide_document(content):
    return Document(
        fd.create_guide_title(content),
        "guides",
    )



def _create_doc_from_file(filepath: str, transform: Callable, create_doc_filemame: Callable):
    """
    Creates a document from a file by reading its content, processing it, and saving the result to a specified location.
    Args:
        filepath (str): The path to the input file.
        transform (function): A function that processes the content of the file.
        create_doc_filemame (function): A function that returns a Document initialized with title and type
    Returns:
        None
    """
    content = read_file_with_fallback(filepath)
    processed_content = transform(content)
    doc = create_doc_filemame(content)

    output_path = f"_docs/{doc.type}/{doc.title}.json"
    ensure_path_exists(output_path)
    with open(output_path, 'w') as output_file:
        output_file.write(str(processed_content))

def _process_files_in_folder(folder_path: str, transform: Callable, create_doc_filemame: Callable):
    """
    Processes all files in the specified folder by applying a transformation and creating a document for each file.
    Args:
        folder_path (str): The path to the folder containing the files to be processed.
        transform (function): A function that takes a file path as input and returns the transformed content.
        create_doc_filemame (function): A function that returns a Document initialized with title and type
    Returns:
        None
    """

    for root, _, files in os.walk(folder_path):
        for each in files:
            file_path = os.path.join(root, each)
            _create_doc_from_file(file_path, transform, create_doc_filemame)


def docify(content_type: str):
    if content_type == "guides":
        _process_files_in_folder(
            "data/documentation/guides", 
            fd.format_elastic_guides,
            define_guide_document,
        )
    
    if content_type == "api-spec":
        _process_files_in_folder(
            "data/documentation/api-spec", 
            fd.format_elastic_api_specs,
            define_api_spec_document,
        )
