from app import ma
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from flask_sqlalchemy import Pagination
from app.models.metric import MetricRecordset, Metric, MetricList, MetricRecordsetValues


class MetricSchema(SQLAlchemySchema):

    class Meta:
        model = Metric
        load_instance = True
        transient = True

    id = auto_field()
    name = auto_field()
    timestamp = auto_field()


class MetricRecordsetSchema(SQLAlchemySchema):

    class Meta:
        model = MetricRecordset
        load_instance = True
        transient = True

    value = auto_field()
    timestamp = auto_field()


class MetricListSchema(ma.Schema):

    class Meta:
        model = MetricList

    metrics = ma.Nested(MetricSchema(many=True))


class MetricRecordsetValuesSchema(ma.Schema):

    class Meta:
        model = MetricRecordsetValues

    values = ma.Nested(MetricRecordsetSchema(many=True))
