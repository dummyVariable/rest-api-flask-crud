from flask_restful import Resource, reqparse
from api.model import CrudModel as db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('league')


def abort_message():
    return {'message' : 'item not found'}


class CrudApp(Resource):

    def get(self):
        return {'app' : 'crud api'}

class CrudAll(Resource):

    def get(self):
        data = db().read_all()
        
        if data:
            return data
        
        return {'message' : 'no items found'}

    def post(self):
        args = parser.parse_args()
        msg = db().create(args)
        if msg:
            return {'message' : 'created'}
        return abort_message()

class CrudByID(Resource):
    

    def get(self, id: int) -> dict:
        data = db().read(id)
        if not data:
            return abort_message()
        
        return data

    def put(self, id: int) -> dict:
        args = parser.parse_args()
        data = db().update(id, args)
        if not data:
            return abort_message()
        return {'message' : 'updated'}
    
    def delete(self, id: int) -> dict:
        data = db().delete(id)
        
        if not data:
            return abort_message()
        return {'message' : 'deleted'}