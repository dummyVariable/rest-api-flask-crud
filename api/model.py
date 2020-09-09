from typing import TypeVar, List

import redis
import json

rc = redis.Redis()
data = {}

class CrudModel:
    counter = 0

    @staticmethod
    def create(item: dict) -> str:
        if not isinstance(item, dict):
            return None
        CrudModel.counter += 1
        item_encoded = json.dumps(item)
        rc.set(CrudModel.counter, item_encoded)
        return 'ok'
    
    @staticmethod
    def read(id: int) -> dict:
        item = rc.get(id)
        if item:
            item_decoded = json.loads(item)
            data = {'name' :item_decoded['name'], 'league' : item_decoded['league']}
            return data
        return None

    @staticmethod
    def read_all() -> List[dict]:
        data = []
        keys = rc.keys()
        if not keys:
            return None
        for key in keys:
            item_decoded = json.loads(rc.get(key))
            item = {'name' :item_decoded['name'], 'league' : item_decoded['league']}
            data.append(item)
        return data

    @staticmethod
    def update(id: int, item: dict) -> str:
        if not isinstance(item, dict):
            return None  
        
        item_encoded = json.dumps(item)
        rc.set(id, item_encoded)

        return 'ok'

    @staticmethod
    def delete(id: int) -> str:
        if not rc.get(id):
            return None
        rc.delete(id)
        return 'ok'

    