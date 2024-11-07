from datetime import datetime, timezone
import json
import re

def _extract_text_between_markers(text: str) -> str:
    """
    Extracts and returns the text found between the first occurrence of double square brackets [[ and ]].
    Args:
        text (str): The input string containing the text to be extracted.
    Returns:
        str: The text found between the first occurrence of [[ and ]]. If no such text is found, returns an underscore ("_").
    """
    
    match = re.search(r'\[\[(.*?)\]\]', text)
    return match.group(1) if match else "_"

def _extract_role(text):
    """
    Extracts roles from the given text.
    This function searches for patterns in the text that match the format [role="role_name"]
    and returns a list of the role names found.
    Args:
        text (str): The input text from which to extract roles.
    Returns:
        list: A list of role names (str) extracted from the text.
    """

    return re.findall(r'\[role="([^"]+)"\]', text)

def _includes_code(text):
    """
    Checks if the given text includes a specific code delimiter.
    Args:
        text (str): The text to be checked.
    Returns:
        bool: True if the text contains the delimiter "--------------------------------------------------", False otherwise.
    """

    return "--------------------------------------------------" in text

def _format_documentation_page_to_doc(source):
    """
    Transforms a documentation page source into a JSON document.
    Args:
        source (str): The source content of the documentation page.
    Returns:
        str: A JSON string representing the transformed documentation page with metadata.
    """
    elastic_host = "https://www.elastic.co/guide/en/elasticsearch/reference/current/"

    doc_title = _extract_text_between_markers(source),
    
    doc = {
        "meta": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "size": len(source),
            
            "url": elastic_host + doc_title[0] + ".html",
            "type": "documentation",
            "role": _extract_role(source),
            "has_code": _includes_code(source),
            "title": doc_title[0],
            "version": "8.15",
        },
        "doc": str(source),
    }
    
    return json.dumps(doc, indent=4)
    

def format_to_doc(source: str) -> json:
    return _format_documentation_page_to_doc(source)

def title(content: str) -> str:
    return _extract_text_between_markers(content)