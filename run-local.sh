python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
flask db init
flask db upgrade
export FLASK_APP=app:app
flask run
