import unittest
from format_docs.elastic_api_spec import format_to_doc


class TestTransformApiSpecToDoc(unittest.TestCase):

    def test_valid_api_spec(self):
        api_spec = '''
        {
            "indices.create": {
                "documentation": {
                    "description": "Creates an index.",
                    "url": "https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html"
                },
                "stability": "stable",
                "response": {
                    "treat_json_as_key_value": true
                },
                "visibility": "public",
                "url": {
                    "paths": ["/{index}"]
                },
                "params": {
                    "pretty": {
                        "type": "boolean",
                        "description": "Pretty format the returned JSON response.",
                        "default": false
                    }
                }
            }
        }
        '''
        result = format_to_doc(api_spec)
        self.assertIn('"api_name": "indices.create"', result)
        self.assertIn('"stability": "stable"', result)
        self.assertIn('"treat_json_as_key_value": true', result)
        self.assertIn('"title": "Creates an index."', result)

    def test_missing_optional_fields(self):
        api_spec = '''
        {
            "indices.create": {
                "documentation": {
                    "description": "Creates an index."
                },
                "stability": "stable"
            }
        }
        '''
        result = format_to_doc(api_spec)
        self.assertIn('"api_name": "indices.create"', result)
        self.assertIn('"stability": "stable"', result)
        self.assertIn('"title": "Creates an index."', result)
        self.assertIn('"url": ""', result)

    def test_empty_api_spec(self):
        api_spec = '{}'
        with self.assertRaises(IndexError):
            format_to_doc(api_spec)

if __name__ == '__main__':
    unittest.main()