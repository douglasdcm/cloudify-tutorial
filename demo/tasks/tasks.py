from cloudify.decorators import operation


@operation
def my_classes_set_property(ctx, dog, **kwards):
    ctx.node.properties["dog_names"] = dog.name
    dogs_name = ctx.node.properties["dog_names"]
    ctx.logger.info("My dog names {0}".format(dogs_name))
    return dogs_name

@operation
def task_demo(ctx, **kwards):
    return ctx.blueprint.id