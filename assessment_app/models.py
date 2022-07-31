# import sqlite3

from flask_sqlalchemy import SQLAlchemy


# testdb = SQLAlchemy()
#
#
# class users(testdb.Model):
#     id = testdb.Column(testdb.Integer, primary_key=True)
#
#     def __repr__(self):
#         return f'<id {self.id}>'




#
# class DataModel:
#     connection = None
#
#     def __init__(self):
#         self.connection = sqlite3.connect('database.db')
#
#         with open('schema.sql') as f:
#             self.connection.executescript(f.read())
#
#     cur = connection.cursor()
#
#     cur.execute("SELECT * from users")
#     print("!!!cur:", cur.fetchall())
#
#     connection.commit()
#     connection.close()
