from flask import Flask
from flask_restful import Api
from api.router import CrudApp, CrudAll, CrudByID

app = Flask(__name__)
api = Api(app)

api.add_resource(CrudApp, '/')
api.add_resource(CrudAll, '/crud')
api.add_resource(CrudByID, '/crud/<int:id>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)