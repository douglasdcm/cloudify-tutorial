from cloudify.decorators import operation


@operation
def taks_with_params(ctx, param_1, **kwargs):
    ctx.logger.info("Message from task with param value {0}.".format(param_1))
    return param_1

@operation
def my_task(ctx, **kwargs):
    ctx.logger.info("Message from my plugin.")

@operation
def task_demo(ctx, **kwards):
    return ctx.node.properties["some_property"]

@operation
def get_runtime_properties(ctx, prop, **kwards):
    ctx.instance.runtime_properties["test_runtime"] = prop
    return ctx.instance.runtime_properties["test_runtime"]

# https://tipsfordev.com/cloudify-get-workflow-s-blueprint-id-and-deployment-id
@operation
def get_blueprint_id(ctx, **kwards):
    id_ = ctx.blueprint.id
    ctx.logger.info("My blueprint id {0}".format(id_))
    return id_

@operation
def get_deployment_id(ctx, **kwards):
    id_ = ctx.deployment.id
    ctx.logger.info("My deployment id {0}".format(id_))
    return id_