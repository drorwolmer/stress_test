from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_apispec.extension import APISpec

app = Flask(__name__)

app.config.update({
    'APISPEC_SPEC':
        APISpec(
            title='Cognigo API',
            version='v1',
            plugins=('apispec.ext.marshmallow',))
})

app_docs = FlaskApiSpec(app)
