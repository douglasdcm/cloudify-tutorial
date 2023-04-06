import os
import tempfile

from cloudify import ctx

webserver_root = tempfile.mkdtemp()
# a property, which is set during runtime, is added to the runtime
# properties of that specific node instance
ctx.instance.runtime_properties['webserver_root'] = webserver_root

webserver_port = 9000 # ctx.node.properties['port']

with open(os.path.join(webserver_root, 'index.html'), 'w') as f:
    f.write('<p>Hello Cloudify!</p>')

command = 'cd {0}; nohup python -m SimpleHTTPServer {1} > /dev/null 2>&1' \
            ' & echo $! > python-webserver.pid'.format(webserver_root, webserver_port)

ctx.logger.info('Starting HTTP server using: {0}'.format(command))
os.system(command)