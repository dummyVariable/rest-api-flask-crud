from typing import TypeVar, List



data = {}

class CrudModel:
    counter = 0

    @staticmethod
    def create(item: dict) -> str:
        if not isinstance(item, dict):
            return None
        CrudModel.counter += 1
        data[CrudModel.counter] = item
        return 'ok'
    
    @staticmethod
    def read(id: int) -> dict:
        return data.get(id)

    @staticmethod
    def read_all() -> List[dict]:
        return data

    @staticmethod
    def update(id: int, item: dict) -> str:
        if not isinstance(item, dict):
            return None  
        if id not in data.keys():
            return None
        data[id] = item
        return 'ok'

    @staticmethod
    def delete(id: int) -> str:
        if id not in data.keys():
            return None
        del data[id]
        return 'ok'