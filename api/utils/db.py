import os

DB_URL = 'postgresql://{username}:{password}@{db_host}:{port}/{db_name}'.format(
    username = os.environ.get('POSTGRES_USER'),
    db_host = os.environ.get('POSTGRES_HOST'),
    password = os.environ.get('POSTGRES_PASSWORD'),
    port = os.environ.get('POSTGRES_HOST_PORT'),
    db_name = os.environ.get('POSTGRES_DB')
)
