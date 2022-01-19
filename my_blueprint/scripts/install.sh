FOLDER="my_blueprint-app11"
pip install --no-input flask waitress
python "/opt/manager/resources/blueprints/default_tenant/${FOLDER}/my_app/app.py"
#BASE_DIR=$(pwd)
#python3 "${BASE_DIR}/my_app/app.py"