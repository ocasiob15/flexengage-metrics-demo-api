from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from app.config import Config
from flask_marshmallow import Marshmallow
from marshmallow.validate import ValidationError
from app.exceptions import ResourceNotFoundException, BadRequestException, UnauthorizedException
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


class SampleApi(Api):

    def handle_error(self, e):
        if isinstance(e, ValidationError):
            print("Failed to validate request")
            code = 400
            data = {
                "message": "Validation error, request could not be processed.",
                "fields": e.messages
            }
        elif isinstance(e, ResourceNotFoundException):
            print(f"Resource not found with id: {e.resource_id}")
            code = 404
            data = {
                "message": e.message,
                "resource_id": e.resource_id
            }
        elif isinstance(e, BadRequestException):
            print("Bad request received")
            code = 400
            data = {
                "message": e.message
            }
        elif isinstance(e, UnauthorizedException):
            print("Unauthorized")
            code = 403
            data = {
                "message": e.message
            }
        else:
            return super(SampleApi, self).handle_error(e)
        return self.make_response(data, code)


app = Flask(__name__)
with app.app_context():

    # General Configurations
    CORS(app)
    api = SampleApi(app)
    ma = Marshmallow(app)
    app.config.from_object(Config())

    @app.route('/docs')
    def docs():
        return render_template('swaggerui.html')

    # Database
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    db.init_app(app)
    from app.models.metric import Metric

    from app.resources.metric_resource import MetricResource, MetricListResource, MetricRecordsetResource

    api.add_resource(MetricListResource, "/metrics")
    api.add_resource(MetricResource, "/metrics/<metric_id>")
    api.add_resource(MetricRecordsetResource, "/metrics/<metric_id>/recordset")
