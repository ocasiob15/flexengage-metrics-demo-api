import os


class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://" \
                              f"{os.getenv('MYSQL_USER', 'admin')}:{os.getenv('MYSQL_PASSWORD', 'password')}" \
                              f"@{os.getenv('MYSQL_HOST', 'localhost')}:{os.getenv('MYSQL_PORT', '3306')}" \
                              f"/sample_service"

    def __init__(self):
        env = os.getenv('ENV', 'local')
        if env == 'local':
            self.local()

    def local(self):
        # You can also use sqlite:///:memory: but app.db is better for migrations
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
        self.SECURE_ENDPOINTS = False
