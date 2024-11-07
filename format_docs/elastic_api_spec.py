import json
from datetime import datetime, timezone


api_specification_details = """

The specification contains:

* The _name_ of the API (`indices.create`), which usually corresponds to the client calls
* Link to the documentation at the <http://elastic.co> website.

  **IMPORANT:** This should be a _live_ link. Several downstream ES clients use
  this link to generate their documentation. Using a broken link or linking to
  yet-to-be-created doc pages can break the [Elastic docs
  build](https://github.com/elastic/docs#building-documentation).
* `stability` indicating the state of the API, has to be declared explicitly or YAML tests will fail
    * `experimental` highly likely to break in the near future (minor/patch), no bwc guarantees.
    Possibly removed in the future.
    * `beta` less likely to break or be removed but still reserve the right to do so
    * `stable` No backwards breaking changes in a minor
* Request URL: HTTP method, path and parts
* Request parameters
* Request body specification

**NOTE**
If an API is stable but it response should be treated as an arbitrary map of key values please notate this as followed

```json
{
  "api.name": {
    "stability" : "stable",
    "response": {
      "treat_json_as_key_value" : true
    }
  }
}
```

## Type definition
In the documentation, you will find the `type` field, which documents which type every parameter will accept.

#### Querystring parameters
| Type  | Description  |
|---|---|
| `list`  | An array of strings *(represented as a comma separated list in the querystring)* |
| `date` | A string representing a date formatted in ISO8601 or a number representing milliseconds since the epoch *(used only in ML)*   |
| `time` | A numeric or string value representing duration |
| `string` | A string value  |
| `enum` | A set of named constants *(a single value should be sent in the querystring)*  |
| `int` | A signed 32-bit integer with a minimum value of -2<sup>31</sup> and a maximum value of 2<sup>31</sup>-1.  |
| `double` | A [double-precision 64-bit IEEE 754](https://en.wikipedia.org/wiki/Floating-point_arithmetic) floating point number, restricted to finite values.  |
| `long` | A signed 64-bit integer with a minimum value of -2<sup>63</sup> and a maximum value of 2<sup>63</sup>-1. *(Note: the max safe integer for JSON is 2<sup>53</sup>-1)* |
| `number` | Alias for `double`. *(deprecated, a more specific type should be used)*  |
| `boolean` | Boolean fields accept JSON true and false values  |

{
  "documentation" : {
    "description": "Parameters that are accepted by all API endpoints.",
    "url": "https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html"
  },
  "params": {
    "pretty": {
      "type": "boolean",
      "description": "Pretty format the returned JSON response.",
      "default": false
    },
    "human": {
      "type": "boolean",
      "description": "Return human readable values for statistics.",
      "default": true
    },
    "error_trace": {
      "type": "boolean",
      "description": "Include the stack trace of returned errors.",
      "default": false
    },
    "source": {
      "type": "string",
      "description": "The URL-encoded request definition. Useful for libraries that do not accept a request body for non-POST requests."
    },
    "filter_path": {
      "type": "list",
      "description": "A comma-separated list of filters used to reduce the response."
    }
  }
}
"""



def _transform_api_spec_to_doc(api_spec: str) -> json:
    """
    Transforms an Elastic API specification into a structured documentation format.
    Args:
        api_spec (str): The JSON string of the API specification.
    Returns:
        str: A JSON string containing the structured documentation.
    The returned JSON string contains the following keys:
        - meta: Metadata about the API specification including:
            - timestamp: The time when the document was created.
            - api_name: The name of the API.
            - stability: The stability level of the API.
            - visibility: The visibility level of the API.
            - main_component: The main component of the API.
            - url: The URL to the API documentation.
            - elastic_url: The constructed URL to the Elastic documentation.
            - treat_json_as_key_value: Whether the response should be treated as key-value JSON.
            - title: The title of the documentation.
            - paths: The URL paths for the API.
            - parameter_types: The types of parameters used in the API.
            - type: The type of the document, which is "api_spec".
        - doc: The original API specification as a string.
    """
    elastic_host = "https://www.elastic.co"

    spec_as_json = json.loads(api_spec)
    
    api_name = list(spec_as_json.keys())[0]
    source = spec_as_json[api_name]
    
    # Extracting main details
    doc_title = source.get("documentation", {}).get("description", "")
    doc_url = source.get("documentation", {}).get("url", "")
    stability = source.get("stability", "")
    response_key_value = source.get("response", {}).get("treat_json_as_key_value", False)
    visibility = source.get("visibility", "public")
    url_paths = source.get("url", {}).get("paths", [])
    params = source.get("params", {})

    
    # Organizing parameters with their type descriptions
    param_types = {param: params[param].get("type", "unknown") for param in params}
    
    # Structuring the output document
    doc = {
        "meta": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "api_name": api_name,
            "stability": stability,
            "visibility": visibility,
            "main_component": api_name if len(api_name.split(".")) == 1 else api_name.split(".")[0],
            "url": doc_url,
            "elastic_url": f"{elastic_host}/{api_name.replace('.', '/')}.html",
            "treat_json_as_key_value": response_key_value,
            "title": doc_title,
            "paths": str(url_paths),
            "parameter_types": str(param_types),
            "type": "api_spec",
        },
        "doc": str(source),
    }
    
    return json.dumps(doc, indent=4)

def format_to_doc(content: str) -> json:
    return _transform_api_spec_to_doc(content)

def title(content: str) -> str:
    return list(json.loads(content).keys())[0]