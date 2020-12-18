import elasticsearch
import elasticsearch.exceptions

class PlaceTypes(object):
    """
    Wrapper class to get WoePlanet/GeoPlanet placetypes from Elasticsearch
    """

    def __init__(self, es, index='placetypes'):
        self.es = es
        self.index = index

    def by_id(self, id):
        try:
            resp = self.es.get(self.index, id)
            if 'found' in resp:
                return resp['_source']
            else:
                return None

        except elasticsearch.exceptions.NotFoundError as _:
            return None

    def by_name(self, name):
        name = name.lower()
        body = {
            'query': {
                'bool': {
                    'must': [
                        {
                            'match': {
                                'shortname': name
                            }
                        }
                    ]
                }
            }
        }
        params = {
            'rest_total_hits_as_int': 'true'
        }
        resp = self.es.search(body=body, index=self.index, params=params)
        if resp['hits']['total'] == 1:
            return resp['hits']['hits'][0]['_source']

        return None
    
    def is_valid(self, value):
        if isinstance(value, int):
            if self.by_id(value):
                return True
            return False
        
        elif isinstance(value, str):
            if self.by_name(value):
                return True
            return False

        return False
