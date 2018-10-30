import elasticsearch
import twstock
from elasticsearch.helpers import bulk

es = elasticsearch.Elasticsearch([{'host': '127.0.0.1', 'port': 9200}])
detail = twstock.realtime.get('2327')
detail['info'].pop('fullname')
detail['info'].pop('channel')
detail.pop('success')

action = [{
    "_index" : "test",
    "_type" : "stock",
    "_source" : detail
}]

success, _ = bulk(es, action, index="test", raise_on_error=True)

doc = {
    "query": {
        "match": {
            "info.code": "2327"
        }
    }
}

results = es.search(index="test", doc_type="stock",body=doc)
for i in results['hits']['hits']:
    print(i)






