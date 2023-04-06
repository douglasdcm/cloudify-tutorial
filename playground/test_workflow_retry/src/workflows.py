from cloudify.decorators import workflow


# If the task 1 retries, the task 2 is not impacted
@workflow
def retry(ctx, **kwargs):
    task_1 = "task_1"
    task_2 = "task_2"

    graph = ctx.graph_mode()
    for instance in ctx.node_instances:
        operation_1 = instance.execute_operation(task_1)
        operation_2 = instance.execute_operation(task_2)

        graph.add_task(operation_1)
        graph.add_task(operation_2)

        graph.add_dependency(operation_2, operation_1)

    return graph.execute()
