#sudo docker run --rm --privileged  -ti -e container=docker -d --name cfy-centos -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /tmp/$(mktemp -d):/run -p 89:80 local/c7-systemd-httpd

BASE_DIR=$(pwd)
FOLDER=plugin
WAGON=custom_plugin_test-1.0-py27-none-manylinux1_x86_64-centos-Core.wgn
BLUEPRINT=blueprint_test_install.yaml
CONTAINER=cfy_manager_local

echo "Zip plugin"
rm ${FOLDER}.zip
rm ${WAGON}
cd ${FOLDER}
python -m build
cd ${BASE_DIR}
zip -r ${FOLDER} ${FOLDER}

echo "Remove old files in container and create new ones"
CMD="docker exec ${CONTAINER} "
${CMD} yum update -y
${CMD} curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
${CMD} python2 get-pip.py
${CMD} pip uninstall wagon
${CMD} pip uninstall wheel
${CMD} pip install wheel==0.34.1
${CMD} pip install wagon==0.3.2

${CMD} rm ${FOLDER}.zip
${CMD} rm ${WAGON} 
${CMD} rm ${BLUEPRINT}
${CMD} rm ${FOLDER}.yaml
${CMD} rm constraints.txt

docker cp ${FOLDER}.zip ${CONTAINER}:/
docker cp ${FOLDER}.yaml ${CONTAINER}:/
docker cp ${BLUEPRINT} ${CONTAINER}:/
docker cp constraints.txt ${CONTAINER}:/

# ${CMD} wagon create ${FOLDER}.zip
# wagon 0.3.2
${CMD} wagon create -s ${FOLDER}.zip -a '--no-cache-dir -c constraints.txt'
# ${CMD} cfy plugins delete 5069fb07-8a7b-4966-b449-4620588c4033
# ${CMD} cfy plugins upload ${WAGON} -y ${FOLDER}.yaml
# ${CMD} cfy blueprint upload ${BLUEPRINT}
${CMD} wagon validate -s ${WAGON}

echo "Copy the wagon CentOS back to host"
docker cp ${CONTAINER}:/${WAGON} .
ls -lh ${WAGON}
echo "Finished"
