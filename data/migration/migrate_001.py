from playhouse.migrate import *

from db.models import User


db = SqliteDatabase('../my_db.db')
migrator = SqliteMigrator(db)

if __name__ == '__main__':
    migrate(
        migrator.add_column('user', 'lieder', User.lieder),
        migrator.add_column('user', 'admin', User.admin),
        migrator.add_column('user', 'archive', User.archive),
        migrator.drop_column('user', 'phone'),
        migrator.drop_column('user', 'status'),
        migrator.drop_column('user', 'user_id'),
    )
na