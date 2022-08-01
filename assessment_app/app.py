import os, time, json

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy, event

from sqlalchemy.sql import func

import assessment_app.testscr
# import assessment_app.models


# import testscr

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    webapp = Flask(__name__)

    webapp.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

    db = SQLAlchemy(webapp)


    class Role(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text, nullable=False)

        def __repr__(self):
            return f'<role {self.id, self.name}>'


    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.Text, nullable=False)
        role_id = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)

        # roles = relationship("Role")
        def __repr__(self):
            return f'<user {self.id, self.username, self.role_id}>'


    ## assessment_app.models.testdb = db
    ## assessment_app.models.users()

    db.drop_all()
    db.create_all()

    role1 = Role(id=1, name='teacher')
    role2 = Role(id=2, name='accountant')
    role3 = Role(id=3, name='manager')
    role4 = Role(id=4, name='clerk')

    user1 = User(username='Vivek', role_id=1)

    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)
    db.session.add(role4)

    db.session.add(user1)
    db.session.commit()


    @webapp.route('/insertdata', methods=['GET', 'POST'])
    def insertdata():
        if request.method == 'GET':
            roles = Role.query.all()
            return render_template('insertdata.html', roles=roles)

        # POST
        print("!!!post called!!", request.json)

        newuser = User(username=request.json['username'], role_id=request.json['roleid'])

        db.session.add(newuser)
        db.session.commit()

        return json.dumps({"msg":"from insertdata"})

    @webapp.route('/parsefile', methods=['GET', 'POST'])
    def parsefile():
        pass


    @webapp.route('/viewdb')
    def showall():
        print("users", User.query.all())
        print("roles", Role.query.all())

        return render_template('viewdb.html')


    @webapp.route('/')
    def hello():
        return 'Hello, World!'

    @webapp.route('/template')
    def index():
        return render_template('index.html')

    return webapp
