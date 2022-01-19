from cloudify.test_utils import workflow_test
from testtools import TestCase


class TestTasks(TestCase):

    @workflow_test(blueprint_path="test_blueprint.yaml")
    def test_task_demo(self, cfy_local):
        cfy_local.execute('generic_workflow')
