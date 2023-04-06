from cloudify.decorators import operation
from cloudify.exceptions import OperationRetry, NonRecoverableError


class AnyError(Exception):
    pass


@operation
def task_2(ctx):
    ctx.logger.info("taks_2 start")
    try:
        if ctx == 1:
            raise OperationRetry(message="retry")
    except OperationRetry as error:
        # does not care if return or not. The retry has the same behavior
        ctx.operation.retry(message=str(error), retry_after=1)
    ctx.logger.info("taks_2 finish")


@operation
def task_1(ctx, arg):
    try:
        ctx.logger.info("taks_1 start")
        ctx.logger.info(ctx.instance.runtime_properties.get('some_property'))
        if arg == 1:
            raise OperationRetry(message="retry")

        if arg == 2:
            raise AnyError()
        ctx.logger.info("taks_1 half")

        rtp = ctx.node.properties.get('some_property')
        ctx.instance.runtime_properties["some_property"] = rtp
        return True
    except OperationRetry as error:
        ctx.instance.runtime_properties["some_property"] = "retry"
        ctx.operation.retry(message=str(error), retry_after=1)
    except Exception as error:
        raise NonRecoverableError(str(error)) from error
    finally:
        ctx.logger.info("taks_1 finish")
        ctx.logger.info(ctx.instance.runtime_properties.get('some_property'))
