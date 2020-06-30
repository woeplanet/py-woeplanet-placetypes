# <img src="https://avatars1.githubusercontent.com/u/29209318?s=32&v=4" width="32" height="32" alt="woeplanet">&nbsp;py-whosonfirst-placetypes

Simple Python wrapper for accessing WoePlanet/GeoPlanet placetypes in Elasticsearch.

*Elasticsearch Health Warning* this wrapper assumes that a) you have an Elasticsearch instance up and running and b) you've already populated ES with the place type JSON definitions.

## Installation

```
sudo pip install -r requirements.txt .
```

## Usage

```
$ python
Python 3.7.7 (default, Mar 10 2020, 15:43:33)
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from elasticsearch import Elasticsearch
>>> from woeplanet.docs.placetypes import PlaceTypes
>>> es = Elasticsearch(['localhost:9200'])
>>> placetypes = PlaceTypes(es)
>>> name = 'LocalAdmin'
>>> pt = placetypes.by_name(name)
>>> pt
{'description': 'One of the tertiary administrative areas within a country', 'shortname': 'LocalAdmin', 'id': 10, 'name': 'Local Administrative Area'}
>>> id = 10
>>> pt = placetypes.by_id(id)
>>> pt
{'description': 'One of the tertiary administrative areas within a country', 'shortname': 'LocalAdmin', 'id': 10, 'name': 'Local Administrative Area'}
```

## See also

* https://github.com/woeplanet/py-woeplanet-es-bootstrap, especially `./bin/index-placetypes.py`
