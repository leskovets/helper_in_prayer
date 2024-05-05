from peewee import *

db = SqliteDatabase('data/my_db.db')


def db_init() -> None:
    with db:
        tables = [User, Story, Plan]
        if not all(table.table_exists() for table in tables):
            db.create_tables(tables)  # создаем таблицы


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db


class User(BaseModel):

    user_id = IntegerField(unique=True)
    chat_id = IntegerField(unique=True)
    user_name = CharField(null=True)
    first_name = CharField(null=True)
    phone = CharField(null=True)
    status = CharField(null=True)
    is_reminders = BooleanField()


class Story(BaseModel):
    chat_id = IntegerField()
    date = DateField()
    is_pray = BooleanField()


class Plan(BaseModel):
    chat_id = IntegerField()
    type_plan = CharField(max_length=10)
    day = IntegerField()
    time = TimeField()
    total_alarm = IntegerField(default=0)
