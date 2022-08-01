import os, time, json, shutil, pathlib

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy, event
import pandas as pd

from werkzeug.utils import secure_filename


from sqlalchemy.sql import func

import assessment_app.testscr
# import assessment_app.models


# import testscr

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(basedir,'fileuploads')

    # print("upload dir:", UPLOAD_FOLDER)
    shutil.rmtree(UPLOAD_FOLDER, ignore_errors=True)
    os.makedirs(UPLOAD_FOLDER)

    webapp = Flask(__name__)
    webapp.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
    webapp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    webapp.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    webapp.config['UPLOAD_EXTENSIONS'] = ['.csv']

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

    db.drop_all()
    db.create_all()

    db.session.commit()

    @webapp.route('/insertdata', methods=['GET', 'POST'])
    def insertdata():
        try:
            if request.method == 'GET':
                roles = Role.query.all()
                return render_template('insertdata.html', roles=roles)

            # handle POST request
            print("!!!post called!!", request.json)

            newuser = User(username=request.json['username'], role_id=request.json['roleid'])

            db.session.add(newuser)
            db.session.commit()

        except Exception as e:
            return json.dumps({"statusmsg": "Error!" + str(e)})

        return json.dumps({"statusmsg": "Added new user!"})

    @webapp.route('/parsefile', methods=['GET', 'POST'])
    def parsefile():
        if request.method == 'GET':
            return render_template('parsefile.html')

        # handle POST request
        try:
            usersfile = request.files['usersfile']
            rolesfile = request.files['rolesfile']

            if usersfile.filename == '' or rolesfile.filename == '':
                return json.dumps({"msg":"file error"})

            usersfile_ext = os.path.splitext(usersfile.filename)[1]
            rolesfile_ext = os.path.splitext(rolesfile.filename)[1]

            if usersfile_ext not in webapp.config['UPLOAD_EXTENSIONS'] or \
                rolesfile_ext not in webapp.config['UPLOAD_EXTENSIONS']:
                return json.dumps({"msg": "file error"})

            # now, save files
            usersfilename = secure_filename(usersfile.filename)
            rolesfilename = secure_filename(rolesfile.filename)

            usersfilepath = os.path.join(webapp.config['UPLOAD_FOLDER'], usersfilename)
            rolesfilepath = os.path.join(webapp.config['UPLOAD_FOLDER'], rolesfilename)

            print("now saving:", usersfilename, rolesfilename)

            usersfile.save(usersfilepath)
            rolesfile.save(rolesfilepath)

            usersdf = pd.read_csv(usersfilepath, skipinitialspace=True)
            rolesdf = pd.read_csv(rolesfilepath, skipinitialspace=True)

            for userrow in usersdf.itertuples():
                db.session.add(User(id=userrow.id, username=userrow.username, role_id=userrow.role_id))

                print("user is:", userrow.username)

            for rolerow in rolesdf.itertuples():
                db.session.add(Role(id=rolerow.id, name=rolerow.name))
                print("role is:", rolerow.name)

            db.session.commit()

        except Exception as e:
            return json.dumps({"statusmsg": "Error! " + str(e)})

        return json.dumps({"statusmsg": "csv files parsed and db created!"})


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
