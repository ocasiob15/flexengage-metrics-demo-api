from flask_restful import Resource
from flask import request
from app.util.page import get_pagination_request_from_args, PageRequest
from datetime import datetime
from app.models.metric import Metric, MetricRecordset, MetricList
from app.schemas.metric_schema import MetricSchema, MetricListSchema, MetricRecordsetSchema, MetricRecordsetValuesSchema
from app.services.metric_service import MetricService
import tzlocal


metric_schema = MetricSchema()
metric_list_schema = MetricListSchema()
metric_recordset_schema = MetricRecordsetSchema()
metric_recordset_values_schema = MetricRecordsetValuesSchema()
metric_service = MetricService()


class MetricResource(Resource):

    def get(self, metric_id):
        metric = metric_service.get_metric(metric_id)
        return metric_schema.dump(metric)

    def put(self, metric_id):
        metric: Metric = metric_schema.load(request.get_json(), partial=("id", "timestamp"))
        metric.id = metric_id
        result = metric_service.update_metric(metric)
        return metric_schema.dump(result), 200, {'content-type': 'application/json'}

    def delete(self, metric_id):
        metric_service.delete_metric(metric_id)
        return 200


class MetricListResource(Resource):

    def get(self):
        page_request: PageRequest = get_pagination_request_from_args(request.args)
        result = metric_service.get_metric_list(page_request)
        return metric_list_schema.dump(result), 200, {'content-type': 'application/json'}

    def post(self):
        metric: Metric = metric_schema.load(request.get_json(), partial=("id", "timestamp"))
        metric.timestamp = datetime.now(tzlocal.get_localzone())
        result: Metric = metric_service.create_metric(metric)
        return metric_schema.dump(result), 201, {'content-type': 'application/json'}


class MetricRecordsetResource(Resource):

    def get(self, metric_id):
        page_request: PageRequest = get_pagination_request_from_args(request.args)
        recordset = metric_service.get_metric_recordset(page_request, metric_id)
        return metric_recordset_values_schema.dump(recordset), 200, {'content-type': 'application/json'}

    def post(self, metric_id):
        recordset: MetricRecordset = metric_recordset_schema.load(request.get_json(), partial=("timestamp"))
        recordset.timestamp = datetime.now(tzlocal.get_localzone())
        recordset.metric_id = metric_id
        result = metric_service.add_metric_record_to_recordset(recordset)
        return metric_recordset_schema.dump(result), 201, {'content-type': 'application/json'}
