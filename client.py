from dotenv import load_dotenv
import os

from elasticsearch import Elasticsearch

load_dotenv()

es_url = os.getenv("ELASTIC_API_HOST")
es_api_key = os.getenv("ELASTIC_API_KEY_EUI")

client = Elasticsearch(
    es_url,
    api_key=es_api_key
)