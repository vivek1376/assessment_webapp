```
Please run following commands to run the demo app on linux:

    create a project directory and cd into it
    $ mkdir assessment_dir
    $ cd assessment_dir
    git clone demo code, make sure to clone in current directory
    $ git clone https://github.com/vivek1376/assessment_webapp.git .
    create python venv
    $ python3 -m venv venv
    install pip3 packages
    $ pip3 install -r requirements.txt
    activate venv
    $ source venv/bin/activate
    run flask app
    $ export FLASK_APP='assessment_app.app:create_app()'
    $ export FLASK_ENV=development
    $ flask run --host=0.0.0.0
    Following api's have been implemented
        localhost:5000/viewdb
        This url opens a web page showing data in User and Role table. Initially both tables will be empty.
        localhost:5000/parsefile
        This opens a form where csv files can be uploaded to populate data in tables. Sample files have been provided in the repo: sampleusers.csv and sampleroles.csv. Status message is displayed upon submitting the form.
        localhost:5000/insertdata
        Add a new user by entering username in a text field and selecting role from a drop-down. Status message is displayed upon submitting the form.

Issues:

    Foreign key constraint has been added but is not being enforced as per default behavior, see https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#foreign-key-support. Adding fix from https://stackoverflow.com/a/7831210
    No data, file validation and sanity checks against injection attacks, etc. performed in backend code in current version v0.1
    csv files are not being checked for any errors, they must be valid

Note:

    libraries used: flask, flask_sqlalchemy, pandas. spectre css framerwork used in current version instead of bootstrap
    I did not have the skeleton code, so code organization may be improper, data model classes User and Role have been added to app.py.
    csv files must have a header
```
