# [WIP] Elastic prototype 1 - docify

## Concept
Here is how the prototype fits in the Elastic stack. Focusing on facilitating the ingestion of data into the elastic environment. The formatter takes in a reference to a file, loads it and format it into something suitable for a search in Elastic.

![Conceptual diagram - Overview](https://github.com/jubonni/elasticproto/blob/first_poc/proto1.png)

___

## Overview

This project provides utilities for processing and transforming documentation files into structured formats. It includes functions for generating NDJSON files from a location of JSON documents, ensuring paths exist, reading files with fallback encoding, creating documents from files, and processing multiple files in a location.

When running locally, can just import files directly in the prototype's folder and run `docify` on this folder, which will loop through all files in the folder data/{folder}.

```python
from documents import docify


docify("guides")
docify("api-spec")

```

TODO: COMING SOON

```python
import format_docs as fd
from documents import docify

doc = docify("path_to_a_file.json", formatter=fd.type.guess)
doc.run_elser()

```


<!-- ## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Proto Notebook](#proto-notebook) -->

## Installation

### Prerequisites

- Python 3.8+
- pip
- venv

### Testing
- pytest

### Steps

1. Clone the repository:
    ```sh
    ...
    ```

2. (Optional) Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### 
TODO

# proto-notebook
See https://github.com/jubonni/elasticproto/blob/first_poc/proto.ipynb

