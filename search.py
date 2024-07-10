from pprint import pprint
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

class Search:
    def __init__(self):
        self.es = Elasticsearch('http://localhost:9200')
        client_info = self.es.info()
        print('Connected to ElasticSearch')
        pprint(client_info.body)
