from cloudify.decorators import operation

@operation
def my_task(ctx, **kwargs):
    ctx.logger.info("Message from my plugin.")

@operation
def task_demo(ctx, **kwards):
    return ctx.node.properties['some_property']
