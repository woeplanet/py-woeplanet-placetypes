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

        except elasticsearch.exceptions.NotFoundError as error:
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
