import logging

import MySQLdb
import sqlalchemy as db
import uuid

engine = db.create_engine("mysql://root:@localhost/autovital")

connection = engine.connect()
metadata = db.MetaData()

# define table that we use for register the new user
table_name = "account"
table = db.Table(table_name, metadata, autoload_with=engine)

data = "erwinyonata"

# SELECT COUNT(*) FROM account
query = db.select(db.func.count("*")).select_from(table).where(table.c.username == f"{data}")
result = connection.execute(query).scalar()

print(result)


