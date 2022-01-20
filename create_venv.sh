VENV=venv_sample
rm -rf ${VENV}
python3.6 venv -m ${VENV}
source ${VENV}/bin/activate
pip install -r requirements.txt

