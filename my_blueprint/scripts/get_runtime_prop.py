import tempfile
from cloudify import ctx

run_time_prop = tempfile.mkdtemp()

# https://docs.cloudify.co/cloudify-plugins-common/_modules/cloudify/context.html#NodeInstanceContext
ctx.logger.info('My property {0}'.format(run_time_prop))
ctx.instance.runtime_properties['my_runtime_prop'] = run_time_prop
