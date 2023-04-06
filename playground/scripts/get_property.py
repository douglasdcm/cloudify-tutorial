from cloudify import ctx

# https://docs.cloudify.co/cloudify-plugins-common/_modules/cloudify/context.html#CloudifyContext
my_prop = ctx.node.properties['some_property']
ctx.logger.info('My property {0}'.format(my_prop))