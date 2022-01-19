rm my_blueprint.zip
zip -r my_blueprint my_blueprint/
echo "-------------------------------"
rm my_plugin.zip
rm my_plugin-*.wgn
path=$(pwd)
cd ./my_blueprint/plugins/
zip -r my_plugin my_plugin/
cd ${path}
echo "-------------------------------"
wagon create my_blueprint/plugins/my_plugin.zip 
