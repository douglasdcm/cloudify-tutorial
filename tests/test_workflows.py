from cloudify.test_utils import workflow_test
from testtools import TestCase


class TestWorkflows(TestCase):

    @workflow_test(path_or_blueprint="test_blueprint.yaml")
    def test_workfow_demo(self, cfy_local):
        actual = cfy_local.execute('generic_workflow')
        self.assertIs(True, actual)
