import format_docs as fd

from documents.document import (
    _create_doc_from_file,
    _process_files_in_folder,
)


def docify(doc_type: str, file_path: str = None):
    """
    Creates documents from files in the data/documentation folder.
    Args:
        doc_type (str): The type of document to create.
        file_path (str): The path to a file to create a document from.
    """

    if file_path:
        _create_doc_from_file(
            file_path,
            doc_type,
            fd.empty_formatter,
            fd.empty_title,
        )
        return


    if doc_type == "guides":
        _process_files_in_folder(
            "data/documentation/guides",
            doc_type,
            fd.format_elastic_guides,
            fd.create_guide_title,
        )
    
    if doc_type == "api-spec":
        _process_files_in_folder(
            "data/documentation/api-spec", 
            doc_type,
            fd.format_elastic_api_specs,
            fd.create_api_spec_title,
        )
