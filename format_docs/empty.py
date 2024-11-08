import json

empty_formatter = lambda *args, **kwargs: ("", json.dumps({"doc": ""}, indent=4))
empty_title = lambda *args, **kwargs: ""
