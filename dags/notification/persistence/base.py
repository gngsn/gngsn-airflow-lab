from peewee import Model, PostgresqlDatabase

DB = PostgresqlDatabase('ums', user='postgres', host='127.0.0.1', password='postgres')


class BaseModel(Model):
    class Meta:
        database = DB
