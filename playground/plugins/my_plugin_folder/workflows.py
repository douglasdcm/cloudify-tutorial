from cloudify.decorators import workflow

@workflow
def workflow_demo(**kwargs):
    return True