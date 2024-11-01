docs = {
    "meta": [
        {
            "args": {
                "query_dsl_path": "https://www.elastic.co/guide/en/elasticsearch/reference/current/"
            }
        }
    ],
    "docs":[
        {
            "type": "documentation",
            "url": "${query_dsl_path}/search-with-elasticsearch.html",
            "source": """Search your data

A search query, or query, is a request for information about data in Elasticsearch data streams or indices.

You can think of a query as a question, written in a way Elasticsearch understands. Depending on your data, you can use a query to get answers to questions like:

What processes on my server take longer than 500 milliseconds to respond?
What users on my network ran regsvr32.exe within the last week?
What pages on my website contain a specific word or phrase?
Elasticsearch supports several search methods:

Search for exact values
Search for exact values or ranges of numbers, dates, IPs, or strings.
Full-text search
Use full text queries to query unstructured textual data and find documents that best match query terms.
Vector search
Store vectors in Elasticsearch and use approximate nearest neighbor (ANN) or k-nearest neighbor (kNN) search to find vectors that are similar, supporting use cases like semantic search.
Run a search
edit
To run a search request, you can use the search API or Search Applications.

Search API
The search API enables you to search and aggregate data stored in Elasticsearch using a query language called the Query DSL.
Search Applications
Search Applications enable you to leverage the full power of Elasticsearch and its Query DSL, with a simplified user experience. Create search applications based on your Elasticsearch indices, build queries using search templates, and easily preview your results directly in the Kibana Search UI.
"""
        },
        {
            "type": "documentation",
            "url": "${query_dsl_path}/",
            "source": """
"""
        },
        {
            "type": "documentation",
            "url": "${query_dsl_path}/",
            "source": """
"""
        },
        {
            "type": "documentation",
            "url": "${query_dsl_path}/",
            "source": """
"""
        },
        {
            "type": "documentation",
            "url": "${query_dsl_path}/",
            "source": """
"""
        },
        {
            "type": "documentation",
            "url": "${host}/",
            "source": """
"""
        },
        {
            "type": "documentation",
            "url": "${host}/",
            "source": """
"""
        },
    ]
}