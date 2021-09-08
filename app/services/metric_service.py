from app import db
from app.models.metric import Metric, MetricRecordset, MetricList, MetricRecordsetValues
from app.exceptions import ResourceNotFoundException
from app.util.timezone import localize
import tzlocal


class MetricService:

    def get_metric(self, id: int) -> Metric:
        metric = Metric.query.filter(Metric.id == id).order_by(Metric.timestamp.asc()).first()
        if metric is None:
            raise ResourceNotFoundException(
                f"Could not find metric with id: {id}",
                id)
        metric.timestamp = localize(metric.timestamp)
        return metric

    def create_metric(self, metric: Metric) -> Metric:
        db.session.add(metric)
        db.session.commit()
        db.session.refresh(metric)
        metric.timestamp = localize(metric.timestamp)
        return metric

    def get_metric_list(self, page_request) -> MetricList:
        metrics = Metric.query.order_by(Metric.timestamp.desc())

        for metric in metrics:
            metric.timestamp = tzlocal.get_localzone().localize(metric.timestamp)

        return MetricList(metrics)

    def update_metric(self, metric: Metric) -> Metric:
        saved_metric: Metric = self.get_metric(metric.id)
        saved_metric.name = metric.name
        db.session.commit()
        saved_metric.timestamp = localize(saved_metric.timestamp)
        return saved_metric

    def delete_metric(self, id: int):
        metric = self.get_metric(id)
        db.session.delete(metric)
        db.session.commit()

    def get_metric_recordset(self, page_request, metric_id) -> MetricRecordsetValues:
        result: [MetricRecordset] = MetricRecordset.query\
            .filter(MetricRecordset.metric_id == metric_id)\
            .order_by(MetricRecordset.timestamp.desc())
        return MetricRecordsetValues(result)

    def add_metric_record_to_recordset(self, recordset: MetricRecordset):
        db.session.add(recordset)
        db.session.commit()
        db.session.refresh(recordset)
        recordset.timestamp = localize(recordset.timestamp)
        return recordset
