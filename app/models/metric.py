from app import db


class MetricRecordset(db.Model):
    __tablename__ = 'metric_recordset'
    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    value = db.Column(db.FLOAT)
    metric_id = db.Column(db.INT, db.ForeignKey('metric.id'))
    metric = db.relationship("Metric", backref=db.backref("metric_recordset", cascade="all, delete-orphan"))
    timestamp = db.Column(db.DateTime)


class Metric(db.Model):
    # This model is prefixed with market_ as lead is a reserved word in MySQL 8.0.2+
    __tablename__ = 'metric'
    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime)


class MetricList:

    def __init__(self, metrics):
        self.metrics = metrics


class MetricRecordsetValues:
    def __init__(self, values):
        self.values = values
