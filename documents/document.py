from typing import Callable, Optional

import format_docs as fd
import os
from utils.file import (
    read_file_with_fallback,
    ensure_path_exists,
)


class Document:
    def __init__(self, doc = None):
        if doc:
            self.title = doc.title
            self.type = doc.type
            self.content = doc.content
            return self

        self.title = None
        self.type = None
        self.content = None

        return None

    @classmethod
    def from_content(cls, content, title_gen: Optional[Callable], doc_type: Optional[str]):
        """
        Creates a Document object from content.
        Args:
            content (str): The content of the document.
            title_gen (function): A function that generates the title of the document.
            doc_type (str): The type of the document.
            Returns:
            Document: The Document object.
        """
        doc = Document()

        doc.content = content
        doc.title = title_gen(content) if title_gen else None
        doc.type = doc_type if doc_type else None

        return doc
    
    def export(self):
        return {
            "title": self.title,
            "type": self.type,
            "content": self.content,
        }


def as_api_spec_document(content):
    return Document(
        title=fd.create_api_spec_title(content), 
        type="api-spec",
        content=content,
    )

def as_guide_document(content):
    return Document(
        title=fd.create_guide_title(content),
        type="guides",
        content=content,
    )

def assemble_doc(
        filepath: str, 
        doc_type: str,
        transform: Optional[Callable] = None, 
        title: Optional[Callable] = None
        ) -> str:
    """
    Assembles a document by reading its content, processing it, and returning the result.
    Args:
        filepath (str): The path to the input file.
        doc_type (str): The type of the document.
        transform (function): A function that processes the content of the file.
        title (function): A function to generate title from file content.
        Returns:
        str: The processed content of the document.
    """

    content = read_file_with_fallback(filepath)

    processed_content = transform(content) if transform else content

    doc = Document.from_content(
        processed_content, 
        title_gen=title, 
        doc_type=doc_type,
    )

    return doc


def _create_doc_from_file(filepath: str, doc_type: str, transform: Callable, create_doc_filemame: Callable):
    """
    Creates a document from a file by reading its content, processing it, and saving the result to a specified location.
    Args:
        filepath (str): The path to the input file.
        transform (function): A function that processes the content of the file.
        create_doc_filemame (function): A function that returns a Document initialized with title and type
    Returns:
        None
    """
    doc = assemble_doc(filepath, doc_type, transform, create_doc_filemame)

    save_doc(doc)

    return doc
    

def save_doc(doc: Document):
    """
    """
    output_path = f"_docs/{doc.type}/{doc.title}.json"

    ensure_path_exists(output_path)

    with open(output_path, 'w') as output_file:
        output_file.write(str(doc.content))

def _process_files_in_folder(folder_path: str, doc_type: str, transform: Callable, create_doc_filemame: Callable):
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
            _create_doc_from_file(file_path, doc_type, transform, create_doc_filemame)

