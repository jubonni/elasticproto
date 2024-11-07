import pytest
import json
from format_docs.elastic_guide import (
    _extract_text_between_markers, 
    _extract_role, 
    _includes_code, 
    _format_documentation_page_to_doc, 
    format_to_doc
)

def test_extract_text_between_markers():
    assert _extract_text_between_markers("This is a [[test]] string.") == "test"
    assert _extract_text_between_markers("No markers here.") == "_"
    assert _extract_text_between_markers("[[Start]] and [[End]]") == "Start"

def test_extract_role():
    assert _extract_role('This is a [role="admin"] test.') == ["admin"]
    assert _extract_role('No roles here.') == []
    assert _extract_role('Multiple [role="user"] roles [role="guest"].') == ["user", "guest"]

def test_includes_code():
    assert _includes_code("This text includes a code delimiter -------------------------------------------------- here.") == True
    assert _includes_code("No code delimiter here.") == False

def test_format_documentation_page_to_doc():
    source = "This is a [[test]] documentation page with [role=\"admin\"] and a code delimiter --------------------------------------------------."
    result = _format_documentation_page_to_doc(source)
    result_json = json.loads(result)
    
    assert result_json["meta"]["title"] == "test"
    assert result_json["meta"]["role"] == ["admin"]
    assert result_json["meta"]["has_code"] == True
    assert result_json["meta"]["size"] == len(source)
    assert result_json["meta"]["version"] == "8.15"
    assert result_json["doc"] == source


def test_valid_documentation_page():
    source = """[[example]]
    --------------------------------------------------
    Title: Example Documentation
    --------------------------------------------------
    This is an example documentation page.
    """
    result = json.loads(format_to_doc(source))
    assert "meta" in result
    assert "timestamp" in result["meta"]
    assert result["meta"]["size"] == len(source)
    assert result["meta"]["url"] == "https://www.elastic.co/guide/en/elasticsearch/reference/current/example.html"
    assert result["meta"]["type"] == "documentation"
    assert result["meta"]["title"] == "example"
    assert result["meta"]["version"] == "8.15"
    assert result["doc"] == source

def test_missing_optional_fields():
    source = """ [[example]]
    --------------------------------------------------
    Title: Example Documentation
    --------------------------------------------------
    """
    result = json.loads(format_to_doc(source))
    assert "meta" in result
    assert "timestamp" in result["meta"]
    assert result["meta"]["size"] == len(source)
    assert result["meta"]["url"] == "https://www.elastic.co/guide/en/elasticsearch/reference/current/example.html"
    assert result["meta"]["type"] == "documentation"
    assert result["meta"]["title"] == "example"
    assert result["meta"]["version"] == "8.15"
    assert result["doc"] == source

def test_empty_documentation_page():
    source = ""
    result = json.loads(format_to_doc(source))
    assert "meta" in result
    assert "timestamp" in result["meta"]
    assert result["meta"]["size"] == len(source)
    assert result["meta"]["url"] == "https://www.elastic.co/guide/en/elasticsearch/reference/current/_.html"
    assert result["meta"]["type"] == "documentation"
    assert result["meta"]["title"] == "_"
    assert result["meta"]["version"] == "8.15"
    assert result["doc"] == source



if __name__ == "__main__":
    pytest.main()