BASE_DIR=$(pwd)
cd ${BASE_DIR}/my_blueprint/plugins/my_plugin_folder
python -m build
cd ${BASE_DIR}
./zip_blueprint.sh